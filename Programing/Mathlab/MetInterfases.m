%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ----------------------------------------------------------------------- %
%            SCRIPT TO TEST THE IMMERSED INTERFACE METHOD                 %
%                                                                         %
%         Author: Reymundo Itza (Jun 2022)                                %
%  Last revision: Jun 2022                                                %
%    Modified by: Reymundo Itza                                           %
% ----------------------------------------------------------------------- %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
close all;
%clc
clear
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                         %
%   IIM for general problem:                                              %
%                                                                         %
%                     (\beta u_x)_x - au_x = f                            %
%                                                                         %
%  with the given jump condition in [u] and [\beta u_x] at the alpha point%
%  and Dirichlet boundary conditions.                                     %
%                                                                         %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%----------------
% Domain options
xI  = 0.0;       % interval [xI,xF]
xF  = 1.0;       % interval [xI,xF]
alpha = 0.72;    % interface location
%----------------
a = 1;           % parameter
%----------------
% Functions
ExampleF = 1;
ExampleB = 1;
%----------------
% Node option
M      = 6;               % Number of test cases
Mnodes = @(n) 10*2^(n-1); % Nodes type
%----------------
% Display options
DisplayPlot  = 1;
DisplayLatex = 1;
DisplayLSM   = 0;
%--------------------------------------------------------------------------
%############# DERIVADAS (HANDLE FUNCTIONS)
if ExampleF==1
    A = 2;
    % Exact solution
    uL   = @(x) cos(A*x);
    uxL  = @(x) -A*sin(A*x);
    uxxL = @(x) -A^2*cos(A*x);

    uR   = @(x) cos(A*x);
    uxR  = @(x) -A*sin(A*x);
    uxxR = @(x) -A^2*cos(A*x);
elseif ExampleF==2
    % Exact solution
    uL   = @(x) x^3/3;
    uxL  = @(x) x^2;
    uxxL = @(x) 2*x;

    uR   = @(x) x^3;
    uxR  = @(x) 3*x^2
    uxxR = @(x) 6*x;
elseif ExampleF==3
    A = 2;
    B = 2;
    % Exact solution
    uL   = @(x) cos(A*x);
    uxL  = @(x) -A*sin(A*x);
    uxxL = @(x) -A^2*cos(A*x);

    uR   = @(x) sin(B*x);
    uxR  = @(x) B*cos(B*x);
    uxxR = @(x) -B^2*cos(B*x);
end

if ExampleB==1
    bL   = @(x) 1 + 0*x;
    bxL  = @(x) 0*x;
    bxxL = @(x) 0*x;

    bR   = @(x) 1 + 0*x;
    bxR  = @(x) 0*x;
    bxxR = @(x) 0*x;

elseif ExampleB==2
    bL   = @(x) 2 + 0*x;
    bxL  = @(x) 0*x;
    bxxL = @(x) 0*x;

    bR   = @(x) 1 + 0*x;
    bxR  = @(x) 0*x;
    bxxR = @(x) 0*x;

elseif ExampleB==3
    bL   = @(x) x^2;
    bxL  = @(x) 2*x;
    bxxL = @(x) 2 + 0*x;

    bR   = @(x) x +1 ;
    bxR  = @(x) 1 + 0*x;
    bxxR = @(x) 0*x;

elseif ExampleB==4
    bL   = @(x) cos(x);
    bxL  = @(x) -sen(x);
    bxxL = @(x) -cos(x);

    bR   = @(x) x^2;
    bxR  = @(x) 2*x;
    bxxR = @(x) 2 + 0*x;
end

%############# Right hand side
% f-
fL = @(x) bL(x)*uxxL(x) + bxL(x)*uxL(x) - a*uxL(x);
fR = @(x) bR(x)*uxxR(x) + bxR(x)*uxR(x) - a*uxR(x);

%my beta , a, rhs
my_beta = @(x) (x<=alpha)*bL(x) + (x>alpha)*bR(x);
my_f    = @(x) (x<=alpha)*fL(x) + (x>alpha)*fR(x);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% WORKSPACE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Solution & Errors
disp('-----------------------------------------')
disp('        **Basic information**')
disp('-----------------------------------------')
fprintf('              Example: %i\n',ExampleF)
fprintf('Number of simulations: %i\n',M)
disp('-----------------------------------------')
NormE1   = zeros(M,1);
NormE2   = zeros(M,1);
OrderOr1 = zeros(M,1);
OrderOr2 = zeros(M,1);

Mvec   = zeros(M,1);
tic
for s=1:M
    %--------------------------------
    % Discretization
    n       = Mnodes(s);
    x       = linspace(xI,xF,n+1)';
    Mvec(s) = n;
    fprintf('Mesh #%d : Grid points:%d \n',s,n+1);
    %--------------------------------
    % Find J: the interval where alpha is
    %############# Hallar la interfase
    for i=1:n
        if  (x(i) <= alpha) && ( alpha <x(i+1) )
            I = i;
            break;
        end
    end

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    h  = x(2)-x(1);
    h2 = h*h;
    n  = length(x)-1;
    %----------------------------------------------------------------------
    % FD at regular grid points
    A1 = zeros(n-1,1);
    A2 = zeros(n-1,1);
    A3 = zeros(n-1,1);
    b  = zeros(n-1,1);
    %############# Escribiendo los coeficientes para el caso continuo
    for i=1:n-1
        xl    = x(i+1) - h/2;
        xr    = x(i+1) + h/2;
        A1(i) = my_beta(xl)/h2 + a/(2*h);
        A3(i) = my_beta(xr)/h2 - a/(2*h);
        A2(i) = -(A1(i)+A3(i));
        b(i)  = my_f(x(i+1));
    end
    %----------------------------------------------------------------------
    % IIM & Jump Contrib.
    %----------------------------------------------------------------------
%     B   = zeros(3,3);
%     Bb  = zeros(3,1);
%#############  Limites laterasl
%     % beta
%     bl   =
%     bxl  =
%     bxxl =
%     br   =
%     bxr  =
%     bxxr =
%     % u
%     ul   =
%     uxl  =
%     ur   =
%     uxr  =
%     % rhs
%     fl   =
%     fr   =
%############# Saltos
%     %-----------
%     % Jumps
%     fJ    =       % [f]
%     uJ    =       % [u]
%     uxJ   =       % [u_x]
%     buxJ  =    % [bu_x]
%     bxuxJ =   % [b_xu_x]
%     %-----------
%############# Distancias hacia alfa
%     % Auxiliary quantities
%     h2l =
%     hl  =
%     hr  =
%     h2r =
%     %--------------------------------
%     % At point x=x(J)
%############# Nuevos coeficientes
%     B(1,1) =
%     B(1,2) =
%     B(1,3) =
%     B(2,1) =
%     B(2,2) =
%     B(2,3) =
%     B(3,1) =
%     B(3,2) =
%     B(3,3) =
%     Bb(1)  =
%     Bb(2)  =
%     Bb(3)  =
%     %-----------
%     gam = B\Bb;
%     CJ  = ;
%     %--------------------------------
%     % Contributions to A*u=b
%     %--------------------------------
%############# Asignaciones
%     A1(I-1) =
%     A2(I-1) =
%     A3(I-1) =
%     b(I-1)  = b(I-1) + CJ;
%     %--------------------------------
%     % At point x=x(J+1)
%############# NNuevos coeficientes
%     B(1,1) =
%     B(1,2) =
%     B(1,3) =
%     B(2,1) =
%     B(2,2) =
%     B(2,3) =
%     B(3,1) =
%     B(3,2) =
%     B(3,3) =
%     Bb(1)  =
%     Bb(2)  =
%     Bb(3)  =
%     %-----------
%     gam  = B\Bb;
%     CJp1 =
%     %--------------------------------
%     % Contributions to A*u=b
%     %--------------------------------
%############# Asignaciones
%     A1(I) =
%     A2(I) =
%     A3(I) =
%     b(I)  = b(I) + CJp1;
    %----------------------------------------------------------------------
    % Boundary conditions
    b(1)   = b(1)   - A1(1)*uL(x(1));
    b(n-1) = b(n-1) - A3(n-1)*uR(x(n+1));
    %----------------------------------------------------------------------
    % Solving linear system
    Uaux = Thomas(A1(2:end),A2,A3(1:n-2),b);
%#############
    Ua   = uL(x(1));
    Ub   = uR(x(n+1));
    U    = [Ua;Uaux';Ub];
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %--------------------------------
    % Exact solution and absolute error
    %############# Solucion exacta
    urealt = zeros(Mvec(s)+1,1);
    for i = 1:I
        urealt(i)    = uL(x(i));
    end
    for i = I+1:Mvec(s)+1
        urealt(i)    = uR(x(i));
    end
    Err       = abs(urealt-U);
    NormE1(s) = norm(Err,inf);
    NormE2(s) = sqrt(sum(Err.^2)/(n+1));
    %--------------------------------
    if s~=1
        ss = s-1;
        div = log((Mvec(s))/(Mvec(ss)));
        OrderOr1(s) = log(NormE1(ss)/NormE1(s))/div;
        OrderOr2(s) = log(NormE2(ss)/NormE2(s))/div;
    end
end
disp('')
disp('-----------------------------------------')
toc
%--------------------------------
% Regression line
Dr      = (xF-xI)*1./Mvec;
Errl    =  NormE1;  % Max norm
logDr   = log(Dr);
logErr  = log(Errl);
[mm1,bb] = MinCuaLin(logDr,logErr);
[mm2,~] = MinCuaLin(logDr,log(NormE2));
xx      = linspace(logDr(1),logDr(end),50);
yy      = mm1*xx + bb;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PLOT AREA
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


if DisplayPlot==1
    ymU  = min(U);
    ymUE = min(urealt);
    yMU  = max(U);
    yMUE = max(urealt);
    ymin  = min(ymU,ymUE);
    ymax  = max(yMU,yMUE);
    yv    = linspace(ymin-0.4*abs(ymin),ymax+0.4*abs(ymax),50);

    hFig1=figure(1);
    set(hFig1,'Position',[100 620 1250 430])
    %----------
    % Solution
    sub1  = subplot(1,3,1);

    hold on
    plot(x,U,'o','LineWidth',2)
    plot(x(1:I),urealt(1:I),'-k','LineWidth',2)
    plot(x(I+1:end),urealt(I+1:end),'-k','LineWidth',2)
    plot(x(I),ymin-0.4*abs(ymin),'x','Color',[0,0.5,0],'LineWidth',2)
    plot(x(I),yv,'.','Color',[0,0.5,0],'LineWidth',2)

    legend('Numerical solution','Analytical solution',...
        'Location','NorthWest')

    text(alpha,ymin-0.4*abs(ymin),'$x_\alpha$',...
        'VerticalAlignment','top','FontSize',14,'interpreter','Latex')
    xlabel('$x$','FontSize',22,'interpreter','Latex')
    ylabel('$u$','FontSize',22,'interpreter','Latex')

    title('Solution')

    ylim([ymin-0.4*abs(ymin) ymax+0.4*abs(ymax)]);
    xlim([x(1) x(end)])
    axis square, box on, grid on
    set(gca,'FontSize',14);

    hold off
    %----------
    % Error plot
    sub2  = subplot(1,3,2);
    hold on

    plot(x,Err,'-k','LineWidth',2)
    plot(x(I),0,'x','Color',[0,0.5,0],'LineWidth',2)

    text(alpha,0,'$x_\alpha$',...
        'VerticalAlignment','top','FontSize',14,'interpreter','Latex')
    xlabel('$x$','FontSize',22,'interpreter','Latex')
    ylabel('$L_\infty$-norm error','FontSize',22,'interpreter','Latex')

    title('Absolute error')

    axis square, box on, grid on
    set(gca,'FontSize',14);
    hold off
    %----------
    % Regression line
    sub3  = subplot(1,3,3);
    Dr  = (xF-xI)*1./Mvec;
    Err =  NormE1; % <<<< Max norm
    logDr   = log(Dr);
    logErr  = log(Err);
    logErr1 = 1.0*(logDr(end)-logDr(1))+logErr(1); % First order
    logErr2 = 2.0*(logDr(end)-logDr(1))+logErr(1); % Second order
    logErr3 = 3.0*(logDr(end)-logDr(1))+logErr(1); % Third order
    hold on

    num1 = plot(Dr,exp(logErr),'*k');
    num2 = plot(exp(xx),exp(yy),'k');
    hal = plot([Dr(1),Dr(end)],[Err(1),exp(logErr1)],'--r');
    fir = plot([Dr(1),Dr(end)],[Err(1),exp(logErr2)],'--b');
    sec = plot([Dr(1),Dr(end)],[Err(1),exp(logErr3)],'--m');
    plot_group = [num1,num2,hal,fir,sec];
    legend(plot_group,'Num.','LSM',...
        'Ord. 1','Ord. 2','Ord. 3','Location','SouthEast')
    title('Error analysis')
    xlabel('$\Delta x$','FontSize',22,'interpreter','Latex')
    ylabel('$L_\infty$-norm error','FontSize',22,'interpreter','Latex')
    set(gca,'XScale','log','YScale','log','FontSize',14);
    set(gca,'YMinorGrid','off');
    box on
    grid on
    hold off
    %------------------------------------------------
    % Eliminate white blanks in the contour plots
    set(gcf, 'Renderer', 'opengl')
    set(gcf,'OuterPosition',0.9*[300 300 1600 700])%[10 30 500 550])
    pos1 = [0.0580 0.15 0.27 0.75];
    pos2 = [0.3820 0.15 0.27 0.75];
    pos3 = [0.7150 0.15 0.27 0.75];
    set(sub1,'position', pos1);
    set(sub2,'position', pos2);
    set(sub3,'position', pos3);
end


%--------------------------------------------------------------
% Display Latex
if DisplayLatex ==1
    disp('')
    disp('______________________________________________')
    fprintf('\n')
    fprintf(' %4i & %.2e & ---    &  %.2e & ---    \\\\ \n', Mvec(1)+1,NormE1(1),NormE2(1))
    for i=2:M
        fprintf(' %4i & %.2e & %.3f  &  %.2e & %.3f  \\\\ \n',...
            Mvec(i)+1,NormE1(i),OrderOr1(i),NormE2(i),OrderOr2(i))
    end
    fprintf('\n')
    disp('______________________________________________')
end

if DisplayLSM ==1
    disp('-----------------------------------------')
    fprintf(' Order by LSM fit (Max norm): %.2f \n',mm1)
    fprintf(' Order by LSM fit (L-2 norm): %.2f \n',mm2)
    disp('-----------------------------------------')
end
