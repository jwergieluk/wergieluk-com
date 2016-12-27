Title: Pricing Credit Default Swaps (CDS)
Author: Julian Wergieluk
Date: 2016-12-27
Category: Blog
Tags: quant-finance, python


The CDS contracts are standardized by ISDA. Some details: 

* Coupon dates are 20th of Mar., Jun., Sep., and Dec.
* Different coupon specification. 100 bp or 500bp with an upfront payment. 

## Simple model of Hull

We use the CDS pricing model described in Hull, p. 510. 

Notation:

* Q(t) is the survival probability function, encoding the risk-neutral
  probability that the default does not occur in the time interval [0,t].
* R is the (constant) recovery rate. 
* C(t) is the coupon payed by the protection buyer of the CDS contract with maturity t.

We make the following simplifying assumptions.

* Flat zero risk-free interest rates, i.e. the discount factors satisfy P(t)=1.
* Spread for Y02 CDS is the spread for Y03 CDS.
* Protection premium is payed yearly.
* Default can only occur mid-year.

The present value of the Y01 CDS protection leg is given by

    C(1)*Q(1) + (1-Q(1)) * C(1)*0.5.

The present value of the Y01 CDS default leg is

    (1-R) * ( 1 - Q(1) ).

This implies

    Q(1) = ( 1-R - 0.5*C(1) )/( 1-R + 0.5*C(1) ).

Similarly, the present value of the Y02 CDS protection leg is given by

    C(2)*Q(1) + C(2)*Q(2) + (1-Q(2))*0.5*C(2),

and the present value of the Y02 CDS default leg is

    (1-R)*(1-Q(2)).

This gives us

    Q(2) = ( 1-R - C(2)*Q(1) + 0.5*C(2)  ) / ( 1-R + 0.5*C(2) ).

### Generalization to the 3-years horizon

We drop the assumption that Y02 and Y03 CDS spreads are equal, and consider the
term structure of survival probabilities ( Q(1), Q(2), Q(3) ) with the
assumption 

    Q(2) = 0.5* ( Q(1) + Q(3) ).

The protection leg pv of the Y03 CDS is 

    C(3)*Q(1) + C(3)*Q(2) + C(3)*Q(3) + (1-Q(3))*0.5*C(3).

The default leg pv of that swap  is

    (1-R)*(1-Q(3)).

This gives the following formula for Q(3)

    Q(3) = ( -1.5*C(3)*Q(1) - 0.5*C(3) + 1-R  ) / ( C(3) + 1-R ).


## Rainer's pricing model

Assume that the protection buyer pays a fixed premium $p$ over a unit nominal,
at dates $t_1, t_2, ..., t_N$, where $t_N$ is the maturity date of the
contract.  We also have a stochastic default time $\tau$, $P$ is the term
structure of risk less bonds, and $\mathbb Q$ is the risk neutral measure. The
time is measured by $\delta(t,s)$.


Present value of the premium leg.
$$\Omega(t, \{t_n\}, p) =   \sum_{n=1}^N p \delta(t_{n-1}, t_n) P(t, t_n) 
\mathbb{E}^\mathbb{Q}_t[\mathbf{1}_{\{\tau > t_n\}}] + 
 \mathbb{E}^\mathbb{Q}_t[ p \delta(I(\tau), \tau) P(t, \tau) \mathbf{1}_{\{ \tau \leq t_N \} } ]
$$

Modeling survival probability $Q(t,T)$ of the underlying entity using default intensities.
$$ Q(t, T) 
= \mathbb{E}^\mathbb{Q}_t[\mathbf{1}_{\{\tau > t_n\}}] 
= \exp \Big( - \int^T_t \lambda(s) ds \Big) $$

Default intensity $\lambda$ can be modeled using parametric families.

Present value of the premium leg
$$
\Omega(t, (t_n), p) =  \sum_{n=1}^N p \delta(t_{n-1}, t_n) P(t, t_n) 
\mathbb{E}^\mathbb{Q}_t[\mathbf{1}_{\{\tau > t_n\}}] +  
 \mathbb{E}^\mathbb{Q}_t[ p \delta(I(\tau), \tau) P(t, \tau) \mathbf{1}_{\{ \tau \leq t_N \} } ] 
$$

Substituting survival probability function.
$$
\Omega(t, \{t_n\}, p) =  p \sum_{n=1}^N \delta(t_{n-1}, t_n) P(t, t_n) Q(t, t_n) +  
 p \int_t^{t_N} \delta(t_{I(s), s}) P(t,s) f_\tau(t,s) ds.
$$

$f_\tau(t,s)$ denotes the density of the default time $\tau$.

<!-- :vim: spelllang=en_us:spell: -->
