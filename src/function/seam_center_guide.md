# Seam center guide

| No. | Max | Min | Unit | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| --- | --- | --- | --- | --- |
| A47 | 1 | 0 | - | Seam center guide:<br>0 = Off<br>1 = On |
| A51 | 7 | 0 | - | Automatic lift mode |
| O89 | 999 | 1 | ms | Activation duration of the seam center guide in the time period T1(100% duty) |
| O90 | 100 | 1 | % | Duty cycle in time period T2(PWM) |

**When to lift automatically**

Automatic lifting seam center guide is associated with three situations: footlifter, bartack(start or end tack) or reverse, and stroke. Mode is seted by **A51**.

- 0 = Toggle seam center guide raise up/down via a manual button;

- 1 = Raising of seam center guide when lifting the sewing foot;
- 2 = Raising of seam center guide when sewing the bartack/reverse;
- 3 = Raising of seam center guide when sewing the bartack/reverse and lifting the sewing foot;
- 4 = Raising of seam center guide when high stroke;
- 5 = Raising of seam center guide when lifting the sewing foot and high stroke;
- 6 = Raising of seam center guide when sewing the bartack/reverse and high stroke；
- 7 = Raising of seam center guide when lifting the sewing foot, sewing the bartack/reverse and high stroke.
