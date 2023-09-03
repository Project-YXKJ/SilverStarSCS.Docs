# Sewing foot lifter

Parameter List
==============

P00
---

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description
     | The description can also start on the next line.
     | value1: text;
     | value2: text.
     
| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| A09 | 1 | 0 | - | Sewing foot lifter active:<br>0 = Off;<br>1 = On |
| T05 | 500 | 1 | ms | Sewing foot lifter power on delay at machine stop, the time is less and the sensitivity is higher, more unexpected foot lifting happen when step pedal back for trim. |
| T06 | 500 | 1 | ms | Machine start up delay after sewing foot lifting turned off |
| T10 | 200 | 1 | ms | Sewing foot lifter power on delay at end of seam, pedal idle position confirm delay time |
| A14 | 1 | 0 | - | Lifting sewing foot automatically during stop in sewing operations:<br>0 = Off;<br>1 = On |
| A15 | 1 | 0 | - | Lifting sewing foot automatically after trim/at segment end:<br/>0 = Off;<br/>1 = On |
| O06 | 1 | 0 | - | Timeout release:<br>0 = Off;<br>1 = On |
| O07 | 30 | 5 | s | The maximum time the foot lifter can keep raised |
| O39 | 1 | 0 | -- | Sewing foot lifter soft down:<br>0 = Off;<br>1 = On |
| O40 | 9 | 1 | - | Soft down power |
| T07 | 999 | 1 | ms | Activation duration of the sewing foot lifter in the time period T1(100% duty) |
| O05 | 100 | 1 | % | Duty cycle in time period T2(PWM) |

**Foot is raised:**

- on the seam:

  by pedal back(position -1)

  or automatically with A14 setted to 1

- after thread has been cut

  by pedal back(position -1 or position -2)

  or automatically with A15 setted to 1

**Holding force of the raised foot:**

the foot lifting is raised by full activation, then it switches automatically to partial activation to reduce the load on the controller and the connected magnets. The full activation period is set with T07 and holding force during partial activation is set with O05.

**Timeout release:**

In order to reduce heat generation, timed release can be set. if parameter O06 is set to 1, the maximum time the foot lifter can keep raised is determined by parameter O07.

**Delay time:**

When pushing the pedal forward, with a raised sewing foot the start up delay, which can be set with parameter T06.
