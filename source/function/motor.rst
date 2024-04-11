.. _motor: 

=====
Motor
=====

Holding force of the motor
==========================

Enable this function by set :option:`A 54` to 1.

This function prevents unwanted wandering of the needle when machine has stopped. 
The effect can be checked by turning the hand wheel.

The maximum time the holding force can keep takes effect is determined by parameter :option:`A 66`.

- If :option:`A 66` equal to 0, it take effect always when stopped.
- If :option:`A 66` is not equal to 0, effective time is the value set by :option:`A 66`.

Quick reference
===============

This table summarizes which parameter should be used for motor:

==================================================================== ========== ==============
Parameter                                                            Authority  See also
==================================================================== ========== ==============
Max. Speed                                                           Technician :option:`S 01`
Min. Speed                                                           Technician :option:`S 02`
Auto Upper Position When Power-on                                    Technician :option:`A 18`
Holding Force                                                        Technician :option:`A 54`
Lock Shaft Slot Angle                                                Technician :option:`A 55`
Position Error Threshold of Lock Shaft Function takes effect         Technician :option:`A 56`
Position Error Threshold of Lock Shaft Function does not take effect Technician :option:`A 57`
Holding Force Mode                                                   Technician :option:`A 66`
Machine Sync Signal Source                                           Technician :option:`O 04`
Input Speed Scaling                                                  Technician :option:`O 36`
Input Speed Scaling                                                  Technician :option:`O 37`
Directions of Motor Rotation                                         Technician :option:`O 67`
Acceleration                                                         Technician :option:`I 01`
Deacceleration                                                       Technician :option:`I 02`
Electrical Angle                                                     Developer  :option:`I 03`
Transmission Ratio                                                   Developer  :option:`I 04`
Kp(CSC-t)                                                            Developer  :option:`I 05`
Divisor of Kp(CSC-t)                                                 Developer  :option:`I 06`
Ki(CSC-t)                                                            Developer  :option:`I 07`
Divisor of Ki(CSC-t)                                                 Developer  :option:`I 08`
Kp(CSC)                                                              Developer  :option:`I 09`
Divisor of Kp(CSC)                                                   Developer  :option:`I 10`
Ki(CSC)                                                              Developer  :option:`I 11`
Divisor of Ki(CSC)                                                   Developer  :option:`I 12`
Upper Output limit(CSC)                                              Developer  :option:`I 13`
Feedforward(CSC)                                                     Developer  :option:`I 14`
Kp(CCC-d)                                                            Developer  :option:`I 15`
Divisor of Kp(CCC-d)                                                 Developer  :option:`I 16`
Ki(CCC-d)                                                            Developer  :option:`I 17`
Divisor of Ki(CCC-d)                                                 Developer  :option:`I 18`
Upper Output limit(CCC-d)                                            Developer  :option:`I 19`
Lower Output limit(CCC-d)                                            Developer  :option:`I 20`
Kp(CCC-q)                                                            Developer  :option:`I 21`
Divisor of Kp(CCC-q)                                                 Developer  :option:`I 22`
Ki(CCC-q)                                                            Developer  :option:`I 23`
Divisor of Ki(CCC-q)                                                 Developer  :option:`I 24`
Upper Output limit(CCC-q)                                            Developer  :option:`I 25`
Lower Output limit(CCC-q)                                            Developer  :option:`I 26`
Encoder Resolution                                                   Developer  :option:`I 27`
Stop Routine Max. Time                                               Developer  :option:`I 28`
Stop mode                                                            Developer  :option:`I 30`
MACHINE ZERO Offset                                                  Developer  :option:`I 33`
Distance(Brake P-S process)                                          Developer  :option:`I 37`
Initial Speed(Brake P-S process)                                     Developer  :option:`I 38`
Terminal speed(Brake P-S process)                                    Developer  :option:`I 39`
Kp(CPC-s)                                                            Developer  :option:`I 40`
Divisor of Kp(CPC-s)                                                 Developer  :option:`I 41`
Kd(CPC-s)                                                            Developer  :option:`I 42`
Divisor of Kd(CPC-s)                                                 Developer  :option:`I 43`
Max. Hold Force Current                                              Developer  :option:`I 46`
Field Weaken                                                         Developer  :option:`I 47`
Field Weakening Effective Speed                                      Developer  :option:`I 48`
Max. Id current                                                      Developer  :option:`I 49`
Upper Output limit(CPC-h)                                            Developer  :option:`I 50`
Lower Output limit(CPC-h)                                            Developer  :option:`I 51`
Kp(CPC-h)                                                            Developer  :option:`I 52`
Divisor of Kp(CPC-h)                                                 Developer  :option:`I 53`
Kd(CPC-h)                                                            Developer  :option:`I 54`
Divisor of Kd(CPC-h)                                                 Developer  :option:`I 55`
==================================================================== ========== ==============

Parameter List
==============

.. option:: S 01
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed by press the pedal to the end position.
     
.. option:: S 02

   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Minimum sewing speed, it is also the needle position up-down speed

     
.. option:: A 18

   -Max  4500
   -Min  100
   -Unit  spm
   -Description  
     | Needle position is automatically moved to upper position after power-on:
     | 0 = Off;
     | 1 = On.
     
.. danger:: 
   Please set A18 parameters carefully, it may cause personal danger.

.. option:: A 54

   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Setting the holding force of the motor after stop:
     | 0 = Off;
     | 1 = On.

.. option:: A 55

   -Max  720
   -Min  1
   -Unit  --
   -Description  The shaft is locked a range within this angle.

.. option:: A 56

   -Max  720
   -Min  1
   -Unit  --
   -Description  When the position error is large than the parameters, the motor will 
                 start to adjust the position.

.. option:: A 57

   -Max  720
   -Min  1
   -Unit  --
   -Description  When the position error is small than the parameters,the motor will 
                 standby. 

.. option:: A 66

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = The motor holds always;
     | Not 0 = The holding force turns off after the time set by this parameter.

.. option:: O 04

   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | 0 = Extern;
     | 1 = Motor.

.. option:: O 36

   -Max  5
   -Min  0
   -Unit  --
   -Description  Speed scaling allows the machine to run at lower speed than the set.

.. option:: O 37

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | In Simple mode, no seam program,no trim,no position, etc, except the motor can run:
     | 0 = Off;
     | 1 = On.

.. option:: O 67

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Counterclockwise;
     | 1 = Clockwise, viewing the motor from handwheel  

.. option:: I 01

   -Max  500
   -Min  150
   -Unit  ms
   -Description  The time for accelerating from 0rpm to 4500rpm

.. option:: I 02

   -Max  500
   -Min  150
   -Unit  ms
   -Description  The time for deaccelerating from 4500rpm to 0rpm

.. option:: I 03

   -Max  4096
   -Min  0
   -Unit  --
   -Description  The offset of electrical angle

.. option:: I 04

   -Max  4096
   -Min  1 
   -Unit  --
   -Description  The number of pulses output by motor encoder corresponding to one
                 rotation of the machine


.. option:: I 05

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Speed Control-trimming 

.. option:: I 06

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Speed Control-trimming

.. option:: I 07

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Speed Control-trimming

.. option:: I 08

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Speed Control-trimming

.. option:: I 09

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Speed Control

.. option:: I 10

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Speed Control

.. option:: I 11

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Speed Control

.. option:: I 12

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Speed Control

.. option:: I 13

   -Max  20
   -Min  1
   -Unit  --
   -Description  Upper Output limit in Closed-loop Speed Control

.. option:: I 14

   -Max  500
   -Min  0
   -Unit  --
   -Description  Feedforward in Closed-loop Speed Control

.. option:: I 15

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Current Control-d axis

.. option:: I 16

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Current Control-d axis

.. option:: I 17

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Current Control-d axis

.. option:: I 18

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Current Control-d axis

.. option:: I 19

   -Max  3276
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Current Control-d axis

.. option:: I 20

   -Max  3276
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Current Control-d axis

.. option:: I 21

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Current Control-q axis

.. option:: I 22

   -Max  99
   -Min  0
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Current Control-q axis

.. option:: I 23

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Ki in Closed-loop Current Control-q axis

.. option:: I 24

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Divisor of Ki in Closed-loop Current Control-q axis

.. option:: I 25

   -Max  3276
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Current Control-q axis

.. option:: I 26

   -Max  3276
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Current Control-q axis

.. option:: I 27

   -Max  9999
   -Min  1
   -Unit  --
   -Description  Lines Per Revolution of the motor encoder

.. option:: I 28

   -Max  9999
   -Min  0
   -Unit  ms
   -Description  The maxmum time of stop routine

.. option:: I 30

   -Max  1
   -Min  0 
   -Unit  --
   -Description
     | Select the mode of reaching the target position:
     | 0 = Speed mode;
     | 1 = Position mode.  

.. option:: I 33

   -Max  1
   -Min  0 
   -Unit  --
   -Description  The offset of between MACHINE ZERO and motor synchronization point.

.. option:: I 37

   -Max  359
   -Min  0 
   -Unit  1°
   -Description  The distance of brake Position-Speed process

.. option:: I 38

   -Max  500
   -Min  100 
   -Unit  spm
   -Description  The initial speed of brake Position-Speed process

.. option:: I 39

   -Max  100
   -Min  20 
   -Unit  spm
   -Description  The terminal speed of brake Position-Speed process


.. option:: I 40

   -Max  9999
   -Min  0 
   -Unit  --
   -Description  Kp in Closed-loop Position Control-stop

.. option:: I 41

   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Position Control-stop

.. option:: I 42

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kd in Closed-loop Position Control-stop

.. option:: I 43

   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kd in Closed-loop Position Control-stop

.. option:: I 46

   -Max  40
   -Min  1
   -Unit  0.1A
   -Description  Maximum current during the motor holding

.. option:: I 47

   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Field weaken for higher speed:
     | 0 = Off;
     | 1 = On.

.. option:: I 48

   -Max  3500
   -Min  2000
   -Unit  rpm  
   -Description  Above this speed, field weakening takes effect.

.. option:: I 49

   -Max  40
   -Min  1
   -Unit  0.1A
   -Description  Maximum Id current during field weakening.

.. option:: I 50

   -Max  500
   -Min  0
   -Unit  --
   -Description  Upper Output limit in Closed-loop Position Control-holding

.. option:: I 51

   -Max  100
   -Min  0
   -Unit  --
   -Description  Lower Output limit in Closed-loop Position Control-holding

.. option:: I 52

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kp in Closed-loop Position Control-holding

.. option:: I 53

   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kp in Closed-loop Position Control-holidng

.. option:: I 54

   -Max  9999
   -Min  0
   -Unit  --
   -Description  Kd in Closed-loop Position Control-holding

.. option:: I 55

   -Max  99
   -Min  1
   -Unit  --
   -Description  Divisor of Kd in Closed-loop Position Control-holidng
