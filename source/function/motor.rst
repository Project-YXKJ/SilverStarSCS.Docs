.. _motor: 

=====
Motor
=====

Holding force when idle
==========================

Enable this function by set :option:`A54` to 1.

This function prevents unwanted wandering of the needle when the machine has stopped.
The effect can be checked by turning the hand wheel.

While the function is in effect, the motor will maintain a certain force to *lock* in 
the current position. However, the *lock* here does not mean *standing still*, if the 
parameters are set improperly, or the motor is in a position where the external force 
is too large/small, the needle bar may vibrate up and down. 

Holding force takes effect when idle:

* for a stop in the seam
* after the end of the seam

The maximum time the holding force can keep takes effect is determined by parameter :option:`A66` :

Equal to 0
   Holding force take effect always when stopped.

Not equal to 0
   holding force only take effect for a certain period of time when stop, and then the motor is released. 
   At this time, the parameter value represents the effective time.

The effect can be set by parameter :option:`I46`, the higher the value set the stronger the holding force.

Quick reference
===============

This table summarizes which parameter should be used for motor:

==================================================================== ========== ==============
Parameter                                                            Authority  See also
==================================================================== ========== ==============
Max. Speed                                                           Technician :option:`S01`
Min. Speed                                                           Technician :option:`S02`
Auto Upper Position When Power-on                                    Technician :option:`A18`
Holding Force                                                        Technician :option:`A54`
Step Angle(CPC-h)                                                    Developer  :option:`A55`
Position Error Threshold takes effect(CPC-h)                         Developer  :option:`A56`
Position Error Threshold does not take effect(CPC-h)                 Developer  :option:`A57`
Holding Force Mode                                                   Technician :option:`A66`
Machine Sync Signal Source                                           Technician :option:`O04`
Input Speed Scaling                                                  Technician :option:`O36`
Input Speed Scaling                                                  Technician :option:`O37`
Directions of Motor Rotation                                         Developer  :option:`O67`
Acceleration                                                         Technician :option:`I01`
Deacceleration                                                       Technician :option:`I02`
Electrical Angle                                                     Developer  :option:`I03`
Transmission Ratio                                                   Developer  :option:`I04`
Kp(CSC-t)                                                            Developer  :option:`I05`
Divisor of Kp(CSC-t)                                                 Developer  :option:`I06`
Ki(CSC-t)                                                            Developer  :option:`I07`
Divisor of Ki(CSC-t)                                                 Developer  :option:`I08`
Kp(CSC)                                                              Developer  :option:`I09`
Divisor of Kp(CSC)                                                   Developer  :option:`I10`
Ki(CSC)                                                              Developer  :option:`I11`
Divisor of Ki(CSC)                                                   Developer  :option:`I12`
Upper Output limit(CSC)                                              Developer  :option:`I13`
Feedforward(CSC)                                                     Developer  :option:`I14`
Kp(CCC-d)                                                            Developer  :option:`I15`
Divisor of Kp(CCC-d)                                                 Developer  :option:`I16`
Ki(CCC-d)                                                            Developer  :option:`I17`
Divisor of Ki(CCC-d)                                                 Developer  :option:`I18`
Upper Output limit(CCC-d)                                            Developer  :option:`I19`
Lower Output limit(CCC-d)                                            Developer  :option:`I20`
Kp(CCC-q)                                                            Developer  :option:`I21`
Divisor of Kp(CCC-q)                                                 Developer  :option:`I22`
Ki(CCC-q)                                                            Developer  :option:`I23`
Divisor of Ki(CCC-q)                                                 Developer  :option:`I24`
Upper Output limit(CCC-q)                                            Developer  :option:`I25`
Lower Output limit(CCC-q)                                            Developer  :option:`I26`
Encoder Resolution                                                   Developer  :option:`I27`
Stop Routine Max. Time                                               Developer  :option:`I28`
Stop mode                                                            Developer  :option:`I30`
MACHINE ZERO Offset                                                  Developer  :option:`I33`
Distance(Brake P-S process)                                          Developer  :option:`I37`
Initial Speed(Brake P-S process)                                     Developer  :option:`I38`
Terminal speed(Brake P-S process)                                    Developer  :option:`I39`
Kp(CPC-s)                                                            Developer  :option:`I40`
Divisor of Kp(CPC-s)                                                 Developer  :option:`I41`
Kd(CPC-s)                                                            Developer  :option:`I42`
Divisor of Kd(CPC-s)                                                 Developer  :option:`I43`
Max. Hold Force Current                                              Developer  :option:`I46`
Field Weaken                                                         Developer  :option:`I47`
Field Weakening Effective Speed                                      Developer  :option:`I48`
Max. Id current                                                      Developer  :option:`I49`
Upper Output limit(CPC-h)                                            Developer  :option:`I50`
Lower Output limit(CPC-h)                                            Developer  :option:`I51`
Kp(CPC-h)                                                            Developer  :option:`I52`
Divisor of Kp(CPC-h)                                                 Developer  :option:`I53`
Kd(CPC-h)                                                            Developer  :option:`I54`
Divisor of Kd(CPC-h)                                                 Developer  :option:`I55`
==================================================================== ========== ==============

Parameter List
==============

.. option:: S01
   
   -Max  4500
   -Min  50
   -Unit  spm
   -Description  Maximum speed by press the pedal to the end position.

.. option:: S02

   -Max  1000
   -Min  50
   -Unit  spm
   -Description  Minimum sewing speed, it is also the needle position up-down speed

.. option:: A18

   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Needle position is automatically moved to upper position after power-on:
     | 0 = Off;
     | 1 = On.
     
.. danger:: 
   Please set A18 parameters carefully, it may cause personal danger.

.. option:: A54

   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Setting the holding force of the motor after stop:
     | 0 = Off;
     | 1 = On.

.. option:: A55

   -Max  720
   -Min  1
   -Unit  --
   -Description  The shaft is locked a range within this angle.

.. option:: A56

   -Max  720
   -Min  1
   -Unit  --
   -Description  When the position error is large than the parameters, the motor will 
                 start to adjust the position.

.. option:: A57

   -Max  720
   -Min  1
   -Unit  --
   -Description  When the position error is small than the parameters,the motor will 
                 standby. 

.. option:: A66

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = The motor holds always;
     | Not 0 = The holding force turns off after the time set by this parameter.

.. option:: O04

   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 0 = Extern;
     | 1 = Motor.

.. option:: O36

   -Max  5
   -Min  0
   -Unit  --
   -Description  Speed scaling allows the machine to run at lower speed than the set.
                 For every 1 increase in the parameter value, it decreases by 1/10

.. option:: O37

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | In Simple mode, no seam program,no trim,no position, etc, except the motor can run:
     | 0 = Off;
     | 1 = On.

.. option:: O67

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Counterclockwise;
     | 1 = Clockwise, viewing the motor from handwheel  

.. option:: I01

   -Max  500
   -Min  150
   -Unit  ms
   -Description  The time for accelerating from 0rpm to 4500rpm

.. option:: I02

   -Max  500
   -Min  150
   -Unit  ms
   -Description  The time for deaccelerating from 4500rpm to 0rpm

.. option:: I03

   -Max  4096
   -Min  0
   -Unit  --
   -Description  The offset of electrical angle

.. option:: I04

   -Max  4096
   -Min  1 
   -Unit  --
   -Description  The number of pulses output by motor encoder corresponding to one
                 rotation of the machine

.. option:: I05

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Speed Control-trimming 

.. option:: I06

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Speed Control-trimming

.. option:: I07

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Speed Control-trimming

.. option:: I08

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Speed Control-trimming

.. option:: I09

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Speed Control

.. option:: I10

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Speed Control

.. option:: I11

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Speed Control

.. option:: I12

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Speed Control

.. option:: I13

   -Max  20
   -Min  1
   -Unit  --
   -Description  Upper Output limit in Closed-loop Speed Control

.. option:: I14

   -Max  500
   -Min  0
   -Unit  --
   -Description  Feedforward in Closed-loop Speed Control

.. option:: I15

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Current Control-d axis

.. option:: I16

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Current Control-d axis

.. option:: I17

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Current Control-d axis

.. option:: I18

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Current Control-d axis

.. option:: I19

   -Max  3276
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Current Control-d axis

.. option:: I20

   -Max  3276
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Current Control-d axis

.. option:: I21

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Current Control-q axis

.. option:: I22

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Current Control-q axis

.. option:: I23

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Current Control-q axis

.. option:: I24

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Current Control-q axis

.. option:: I25

   -Max  3276
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Current Control-q axis

.. option:: I26

   -Max  3276
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Current Control-q axis

.. option:: I27

   -Max  9999
   -Min  1
   -Unit  --
   -Description  Lines Per Revolution of the motor encoder

.. option:: I28

   -Max  9999
   -Min  0
   -Unit  ms
   -Description  The maxmum time of stop routine

.. option:: I30

   -Max  1
   -Min  0 
   -Unit  --
   -Description
     | Select the mode of reaching the target position:
     | 0 = Speed mode;
     | 1 = Position mode.  

.. option:: I33

   -Max  1
   -Min  0 
   -Unit  --
   -Description  The offset of between MACHINE ZERO and motor synchronization point.

.. option:: I37

   -Max  359
   -Min  0 
   -Unit  1°
   -Description  The distance of brake Position-Speed process

.. option:: I38

   -Max  500
   -Min  1
   -Unit  spm
   -Description  The initial speed of brake Position-Speed process

.. option:: I39

   -Max  100
   -Min  0 
   -Unit  spm
   -Description  The terminal speed of brake Position-Speed process

.. option:: I40

   -Max  9999
   -Min  0 
   -Unit  --
   -Description  Kp in Closed-loop Position Control-stop

.. option:: I41

   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Position Control-stop

.. option:: I42

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kd in Closed-loop Position Control-stop

.. option:: I43

   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kd in Closed-loop Position Control-stop

.. option:: I46

   -Max  40
   -Min  1
   -Unit  0.1A
   -Description  Maximum current during the motor holding

.. option:: I47

   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Field weaken for higher speed:
     | 0 = Off;
     | 1 = On.

.. option:: I48

   -Max  4500
   -Min  50
   -Unit  rpm  
   -Description  Above this speed, field weakening takes effect.

.. option:: I49

   -Max  40
   -Min  1
   -Unit  0.1A
   -Description  Maximum Id current during field weakening.

.. option:: I50

   -Max  500
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Position Control-holding

.. option:: I51

   -Max  100
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Position Control-holding

.. option:: I52

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Position Control-holding

.. option:: I53

   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Position Control-holidng

.. option:: I54

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kd in Closed-loop Position Control-holding

.. option:: I55

   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kd in Closed-loop Position Control-holidng
