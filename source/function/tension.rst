.. _tension:

==============
Thread tension
==============

*Thread tension procedure:*

The thread tension power on when position is reached with :option:`D 13` and power off 
when position is reached with :option:`D 14` during thread cutting.

Solenoid valve or electromagnet?
================================

If tension is controlled by electromagnet not solenoid valve, you need to be careful
when setting tha value of :option:`O 75`. Over premissible power on time, the electromagnet
may burn out, thus a electromagnet with a small value of :option:`O 75` is protected form damage.

Automation rules
================

Automation rules allow tenison to automate actions under certain working conditions.

How automation rules work:

During foot lifting
-------------------

Adjust parameter of the thread tension during active foot lift: the mode for thread
tension is determined by parameter :option:`A 27`, the default value is 2.

During 2nd Sewing foot stroke
-----------------------------

Adjust parameter of the sewing foot stroke during active the second thread tension:
the mode is determined by parameter :option:`A 28`, the default value 1.

Quick reference
===============

This table summarizes which parameter should be used for tension:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Status of Additional Thread Tension                  Operator   :option:`A 26`
Auto mode for tension at foot lifting                Operator   :option:`A 27`
Auto Additional Thread Tension                       Operator   :option:`A 28`
Start Tension Position                               Technician :option:`D 13`
Stop Tension Position                                Technician :option:`D 14`
Time(t1)                                             Developer  :option:`O 49`
Duty cycle(t2)                                       Developer  :option:`O 50`
Tension Max. Lifting Time                            Developer  :option:`O 75`
Time(t1)                                             Developer  :option:`O 86`
Duty cycle(t2)                                       Developer  :option:`O 87`
Addition tension solenoid work mode                  Developer  :option:`O 88`
==================================================== ========== ==============

Parameter List
==============

.. option:: A 26
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  Status of the additional tension solenoid(read only)

.. option:: A 27

   -Max  3
   -Min  0
   -Unit  --
   -Description
     | Mode for lifting the tension during active sewing foot lift:
     | 0 = tension is not lifted;
     | 1 = tension is lifted as the foot is lifted during sewing;
     | 2 = tension is lifted after trim;
     | 3 = tension is lifted as the foot is lifted during sewing and after trim.
     
.. option:: A 28
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | If the second stroke active,the additional thread tenson is automatically activated:
     | 0 = Off;
     | 1 = On.    

.. option:: D 13
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of tenison is activated during trimming

.. option:: D 14
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Position when the magnet of tension is deactivated during trimming

.. option:: O 49
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Tension:activation duration of in :term:`time period t1` 
                 (100% duty cycle)

.. option:: O 50

   -Max  100
   -Min  1
   -Unit  %
   -Description  Tension:duty cycle[%] in :term:`time period t2`.

.. option:: O 75
   
   -Max  9999
   -Min  0
   -Unit  ms
   -Description 
     | 0 = Always Lifting;
     | Not 0 = This parameter sets the power-off time.
     
.. option:: O 86
   
   -Max  500
   -Min  1
   -Unit  ms
   -Description  Additional Tension:activation duration of in :term:`time period t1`
                 (100% duty cycle)

.. option:: O 87
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Additional Tension:duty cycle[%] in :term:`time period t2`.

.. option:: O 88
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = solenoid on,tension off;
     | 1 = solenoid on,tension on.
