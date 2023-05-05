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

面线张力电磁铁（阀）的动作穿插于剪线动作之中，在剪线动作开始之后，于 D13 角 1° 动作，D14 角 1° 释放。

面线张力机构类型：O88 设定面线张力机构是电磁铁还是电磁阀，此 Parameter 值设置与实际机型配置相符，当为电磁阀式时，穿线模式可用，而为电磁铁式请勿使用穿线模式以免烧毁电磁铁。

压脚与缝线张力的关系：对于面线张力机构为电磁铁的机型，反踩压脚时一般通过机械结构控制挺线动作；面线张力机构为电磁阀的机型，反踩压脚与挺线的关系可以通过 A27 Parameter 来控制，默认值为 2。

切换至第二交互量时自动加大面线张力：由正常交互量切换至第二交互量时，依据 A28 设置的选项，缝线张力随之变动。

压脚或者穿线时挺线限时：抬压脚或者输入按键被配置为穿线模式时，系统会自动打开挺线以方便操作工进行穿线操作，但是请注意：**如果挺线机构使用的是电磁阀，那么可以将 O75 设置为 0；如果使用的是电磁铁，请务必不要将 O75 设置为 0 以防止电磁铁烧坏**。

**Sewing foot stroke**

The thread tension power on when position is reached with D13 and power off when position is reached with D14 during thread trimming.

Adjust parameter of the thread tension during active foot lift: the mode for thread tension is determined by parameter A27, the default value is 2.

Adjust parameter of the sewing foot stroke during active the second thread tension: the mode is determined by parameter A28, the default value 1.
