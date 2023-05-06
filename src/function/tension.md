# Thread tension

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| A27 | 3 | 0 | - | Mode for lifting the needle thread tension during active sewing foot lift:<br>0 = Needle thread tension is not lifted;<br>1 = The thread tension is lifted as the sewing foot are lifted during sewing;<br>2 = The thread tension is lifted after thread trim;<br>3 = The thread tension is lifted as the sewing foot are lifted during sewing and after thread trim |
| A28 | 3 | 0 | - | Coupling of additional thread tension with quick stroke height adjustment, if the second foot stroke is switched on, the second thread tension is automatically activated<br>0 = Off;<br>1 = On |
| D13 | 359 | 0 | 1° | Thread tension power on angle |
| D14 | 359 | 0 | 1° | Thread tension power off angle |
| O49 | 500 | 1 | ms | Activation duration of the main thread tension in the time period T1(100% duty) |
| O50 | 100 | 1 | % | Duty cycle in time period T2(PWM) |
| O75 | 9999 | 0 | ms | Timed release option, thread tension power on time:<br>0 = Can be powered on all the time;<br>N = Automatically release after the time set by O75 |

**Additional thread tension**

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| O86 | 500 | 1 | ms | Activation duration of the addition thread tension in the time period T1(100% duty) |
| O87 | 100 | 1 | % | Duty cycle in time period T2(PWM) |
| O88 | 1 | 0 | - | NC Solenoid Valve or NO Solenoid Valve, used to additional tension:<br> 0 = power on, the additional tension lifted;<br> 1 = power off, the additional tension lifted |
| A26 | 1 | 0 | - | Additional thread tension state(read only):<br> 0 = Press on;<br> 1 = Lifted |

**During thread cutting:**

The thread tension power on when position is reached with D13 and power off when position is reached with D14 during thread trimming.

**During foot lifting:**

Adjust parameter of the thread tension during active foot lift: the mode for thread tension is determined by parameter A27, the default value is 2.

**During 2nd Sewing foot stroke:**

Adjust parameter of the sewing foot stroke during active the second thread tension: the mode is determined by parameter A28, the default value 1.

**Electromagnetor solenoid valve:**

If tension is controlled by electromagnet not solenoid valve, you need to be careful when setting tha value of **O75**. Over premissible power on time, the electromagnet may burn out, thus a electromagnet with a small value of **O75** is protected form damage.
