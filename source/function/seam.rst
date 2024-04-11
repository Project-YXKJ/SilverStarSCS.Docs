.. _seam:

====
Seam
====

Basic concepts
==============

Seam
   A *seam*, usually is divided into three parts: start bartack, middle sewing,
   end bartack and thread cutting. 

   A seam starts from stepping on pedal :term:`POSITION 1` for the first time, 
   and ends when stepping on :term:`POSITION -2`.

Program
   A *sewing program*, contains at least one seam. Let's call it Seam-01, 
   Seam-02 ... Seam-n, program controls them sewing automatically, 
   when Seam-n is finished, program end.

Fixed stitches program
======================

Fixed stitch sewing is a sewing program that allows users to freely program. 
Up to 25 seam segments can be programmed, each with a maximum of 99 stitches.

The functions of the sewing program are divided into two areas: the global 
functions related to the sewing program and the local functions related to the
seam segment.

*Global functions:*

- Soft start

*Local functions:*

- Number of stitches
- Start/end bartack
- Thread clamp
- Thread trim
- Needle position when sewing stops
- Automatic elevation of sewing foot when sewing stops
- Automatic elevation of sewing foot after thread trim(seam end)

The seam segment whose stitch number is equal to 0 is considered as the end 
of the program. If the stitch number of the next segment is 0, the program will 
return to the first segment.

After any seam section ends, if you step on the pedal :term:`POSITION -2`, 
the whole program will be ended. If the thread trimming has not been executed 
at this time, the thread trimming will be executed and return to the first section,
otherwise program will be directly returned to the first section.

Correction(Needle up/down)
==========================

If :option:`A 03` is equal to 0:

When press the key, the needle moves form the current position to the position 
set by parameter :option:`D 15` or :option:`D 16`, which one is the closest, 
the target position is that one. 

E.g, current position is 40 degrees, :option:`D 15` is 70, :option:`D 16` is 200, 
when you press the button, the motion trace is 
``Position 40 => 70 => 200 => 70 => 200 ...`` .

If :option:`A 03` is equal to 1:

when you press the button, two cases: if you set stop at upper position, 
the needle moves form the current position to the position set by parameter :option:`D 01`. 
if you set stop at lower position, the needle moves form the current position to the 
position set by parameter :option:`D 02`:

E.g, current position is 40 degrees, :option:`D 01` is 70, :option:`D 02` is 200, 
if :option:`A 01` is 0, when you press the button, the motion trace is 
``Position 40 => 200 => 200 => 200 ...`` ;
if :option:`A 01` is 1, when you press the button, the motion trace is 
``Position 40 => 70 => 70 => 70 ...`` ;

Quick reference
===============

This table summarizes which parameter should be used for seam:

============================================================ ========== ==============
Parameter                                                    Authority  See also
============================================================ ========== ==============
Speed in W-Sewing                                            Operator   :option:`S 05`
Speed in Program Sewing                                      Operator   :option:`S 06`
Needle Position                                              Operator   :option:`A 01`
Auto Sewing for Program Sewing                               Operator   :option:`A 02`
Correction mode                                              Operator   :option:`A 03`
Mode After Start Bartack in Programmed Sewing                Operator   :option:`A 16`
Auto End bartack and Trim when Programmed Sewing is finished Operator   :option:`A 17`
Correction Mode                                              Operator   :option:`A 30`
Manual Revserse SW.                                          Operator   :option:`A 31`
Upper Needle Position                                        Technician :option:`D 01`
Lower Needle Position                                        Technician :option:`D 02`
The minimum angle of Off reverse key function                Operator   :option:`D 11`
The maximum angle of Off reverse key function                Operator   :option:`D 12`
Correction:Upper Position                                    Operator   :option:`D 15`
Correction:Lower Position                                    Operator   :option:`D 16`
Sewing mode                                                  Operator   :option:`D 18`
Correction Timming                                           Operator   :option:`O 69`
============================================================ ========== ==============

Parameter List
==============

.. option:: S 05
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed in W-Sewing

.. option:: S 06
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Maximum speed in programmed stitches sewing

.. option:: A 01

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Postion of the needle when sewing stop:     
     | 0 = in the material;
     | 1 = upper needle position.

.. option:: A 02
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = The middle speed of the sewing is controlled by the pedal;
     | 1 = The sewing is performed automatically.  

.. option:: A 03
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Half stitch;
     | 1 = One stitch

.. option:: A 16
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | After start tacking is finished in programmed sewing:
     | 0 = machine stops and must restart with the pedal;
     | 1 = sewing continues after end.

.. option:: A 17
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Whether end tacking and trim is automatically activated at seam end im programmed seam:
     | 0 = continue by pedal;
     | 1 = automatic.

.. option:: A 30

   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = single correction;
     | 1 = continuous correction.

.. option:: A 31
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | 0 = Normal;
     | 1 = Reverse at stop.


.. option:: D 01
  
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Needle in the upper position.

.. option:: D 02
  
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Needle in the lower position.

.. option:: D 11
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  If the needle position is greater than this angle, the manual reverse
                 sewing button will not work.

.. option:: D 12

   -Max  359
   -Min  0
   -Unit  1°
   -Description  If the needle position is greater than this angle, the manual reverse
                 sewing button will not work.

.. option:: D 15
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Upper needle position in correction mode.

.. option:: D 16
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Lower needle position in correction mode.

.. option:: D 18
   
   -Max  3
   -Min  1
   -Unit  --
   -Description  Sewing mode(read only).

.. option:: O 69
   
   -Max  1
   -Min  0
   -Unit  --
   -Description  
     | Choose when you can correction:
     | 0 = Unavailable after trim;
     | 1 = Available during machine stop.
