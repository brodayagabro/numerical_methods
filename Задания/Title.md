# Asymptotics of Localized Solutions of the One-Dimensional Wave Equation with Variable Velocity

#### Equestions
$\begin{cases} 
    \mu^2u_{tt}(x, t) + \mu^2\frac{\partial}{\partial x} c(x) \frac{\partial}{\partial x} u(x, t) = 0\\
    u_{t=0} = V(\frac{x}{\mu} - \frac{a}{\mu}) \\
    u_{t, t=0} = 0
\end{cases}$

#### Characteristics
$\begin{cases}
    \dot{x} = \pm c(x) \\
    x_{t=0} = a
\end{cases}$

#### Theorem
$
\textbf{1. }
    u(x, t) = \frac{1}{2}\Sigma_{\pm}{\sqrt{\frac{c_0}{c(X^{\pm}(t))}}
        V(\frac{c_0 \cdot (x-X^{\pm}(t)}{c(X^{\pm}(t))\cdot\mu}} + O(\mu|log\mu|)
$

$
\textbf{2. }
    u(x,t) = \frac{1}{2}\Sigma_{\pm}\sqrt{\frac{c_0}{c(x)}} 
    V(\frac{c_0(T^{\pm}(x)\mp t)}{\mu}) + O(\mu|log\mu|)
$

$    T^{\pm}(X(t, a)) = \pm\int\limits_a^{X^{\pm}(t, a)}\frac{dx}{c(x)}$

## Issue
задания по статье:
1) Для одной из формул посчитать невязку аналитически и численно(подставлением формулы в волновое уравнение)
2) Запрогать обе формулы и сравнить разность решений с невязкой
