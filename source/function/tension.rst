.. _tension:

==============
Thread tension
==============

Solenoid valve or electromagnet?
================================

If tension is controlled by electromagnet not solenoid valve, you need to be careful
when setting tha value of :option:`O75`. Over premissible power on time, the electromagnet
may burn out, thus a electromagnet with a small value of :option:`O75` is protected form damage.

How it works during thread cutting?
===================================

Thread tension procedure:

The thread tension power on when position is reached with :option:`D13` and power off 
when position is reached with :option:`D14` during thread cutting.

Mode needle thread tension at sewing foot lift
==============================================

When the foot is lifted, there are two cases: during sewing and after thread trimming,
There are 4 options for the automatic mode of thread tension. 

The mode is set by parameter :option:`A27`:

* 0 = tension is not lifted;
* 1 = tension is lifted as the foot is lifted during sewing;
* 2 = tension is lifted as the foot is lifted after thread trim;
* 3 = tension is lifted as the foot is lifted during sewing and after trim.

Automation rules for additional thread tension
==============================================

Automatic activate additional thread tension is associated with three situations: 

* Stroke
* Bartack at seam begin
* Bartack at seam end

How automation rules work
-------------------------

If the second sewing foot stroke is switched on, the additional thread tension is 
automatically activated, when the stroke has returned to the normal position, the additional
thread tension has also returned to normal settings.

During bartack at seam begin, the additional thread tension is automatically activated, when the 
bartack completes, the additional thread tension has also returned to normal settings.

During bartack at seam end, the additional thread tension is automatically activated, when the
bartack completes, the additional thread tension has also returned to normal settings.

The mode is set by parameter :option:`A28`, you can use the following table to quickly
check the parameter values ​​you need to set:

====== ====== ===================== =================== 
Value  Stroke Bartack at seam begin Bartack at seam end
====== ====== ===================== ===================
0      Off    Off                   Off
1      On     Off                   Off
2      Off    On                    Off
3      On     On                    Off
4      Off    Off                   On
5      On     Off                   On
6      Off    On                    On
7      On     On                    On
====== ====== ===================== ===================

Quick reference
===============

This table summarizes which parameter should be used for tension:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Status of Additional Thread Tension                  Developer  :option:`A26`
Auto mode for tension at foot lifting                Technician :option:`A27`
Auto Additional Thread Tension                       Technician :option:`A28`
Start Tension Position                               Technician :option:`D13`
Stop Tension Position                                Technician :option:`D14`
Time(t1)                                             Developer  :option:`O49`
Duty cycle(t2)                                       Developer  :option:`O50`
Tension Max. Lifting Time                            Developer  :option:`O75`
Time(t1)                                             Developer  :option:`O86`
Duty cycle(t2)                                       Developer  :option:`O87`
Addition tension solenoid work mode                  Developer  :option:`O88`
==================================================== ========== ==============

Parameter List
==============

.. option:: A26
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Status of the additional tension solenoid(read only).

.. option:: A27

   -Max  3
   -Min  0
   -Unit  --
   -Description
     | Mode for lifting the tension during active sewing foot lift:
     | 0 = tension is not lifted;
     | 1 = tension is lifted as the foot is lifted during sewing;
     | 2 = tension is lifted after trim;
     | 3 = tension is lifted as the foot is lifted during sewing and after trim.
     
.. option:: A28
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Auto mode for additional thread tension:
     | 0 = Off;
     | 1 = Automatically activated when the second sewing foot stroke is switched on;
     | 2 = Automatically activated during bartack at seam begin; 
     | 3 = 1 & 2;
     | 4 = Automatically activated during bartack at seam end;
     | 5 = 1 & 4;
     | 6 = 2 & 4;
     | 7 = 1 & 2 & 4.

.. option:: D13
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of tenison is activated during trimming.

.. option:: D14
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of tension is deactivated during trimming.

.. option:: O49
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Tension:activation duration of in :term:`time period t1` (100% duty cycle).

.. option:: O50

   -Max  100
   -Min  1
   -Unit  %
   -Description  Tension:duty cycle[%] in :term:`time period t2`.

.. option:: O75
   
   -Max  9999
   -Min  0
   -Unit  ms
   -Description 
     | 0 = Always Lifting;
     | Not 0 = This parameter sets the power-off time.
     
.. option:: O86
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Additional Tension:activation duration of in :term:`time period t1` (100% duty cycle).

.. option:: O87
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Additional Tension:duty cycle[%] in :term:`time period t2`.

.. option:: O88
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = solenoid on,tension off;
     | 1 = solenoid on,tension on.
