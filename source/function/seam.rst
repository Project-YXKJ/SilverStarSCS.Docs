Seam
====

Seam
    A *seam*, usually is divided into three parts: start backtack, middle sewing, end
    backtack and thread trimming.

    A seam starts from pedal forward for the first time, and ends when pedal full
    heelback(position -2), i.e. thread trimming marks the end.

    - Free seam
    - Stitch Counting seam
    - W seam

Program
    A *sewing program*, contains at least one seam. Let's call it *Seam-01* , *Seam-02*
    ... *Seam-n* , program controls them sewing automatically, when *Seam-n* is
    finished, program end. After that, you can restart the loop.

Program with Free seam
----------------------

Program with Free seam is a special sewing program, it has only one seam section, and
there is no needle limit in the middle section.

Program with Stitch counting seam
---------------------------------

Program with Stitch counting seam is a sewing program that contains up to 25 stitch
counting seams, each section can be programmed with a maximum of 99 stitches.

The functions of the sewing program are divided into two areas: the global functions
related to the sewing program and the local functions related to the seam section.

**Global functions**

- Soft start

**Local functions**

- Number of stitches
- Start/End backtack
- Thread clamp
- Thread trimmer
- Needle position when sewing stops
- Automatic sewing foot lift when sewing stops
- Automatic sewing foot lift after thread trim(seam end)

The seam section with zero stitches in the middle section is considered as the end of
the program. When the program reaches such a seam, it returns to the first section.

After any seam section ends, if you press the pedal full heelback(position -2), the
whole program will be ended. If the thread trimming has not been executed at this time,
the thread trimming will be executed and return to the first section, otherwise program
will be directly returned to the first section.

Program with W seam
-------------------

Program with W seam is a special sewing program, it has only one seam section, and there
is no start/end backtack, the program will automatic complete when step the pedal
forward.

The total number of sections is defined as E, range 1~15. The number of stitches in the
first section is defined as A, the second section is defined as B, the third section is
defined as C, and the remaining sections is D.

When the program is finished, the pedal must be step back to position 0(neutral) and
then be step forward to start the next sewing.

Correction(Needle up/down)
--------------------------

If :option:`A03` is equal to 0:

When press the key, the needle moves form the current position to the position set by
parameter :option:`D15` or :option:`D16`, which one is the closest, the target position
is that one.

E.g, current position is 40°, :option:`D15` is 70°, :option:`D16` is 200°, when you
press the button, the motion trace is ``Position 40° => 70° => 200° => 70° => 200° ...``
.

If :option:`A03` is equal to 1:

when you press the button, two cases: if you set stop at upper position, the needle
moves form the current position to the position set by parameter :option:`D01`. if you
set stop at lower position, the needle moves form the current position to the position
set by parameter :option:`D02`:

E.g, current position is 40°, :option:`D01` is 70°, :option:`D02` is 200°, if
:option:`A01` is 0, when you press the button, the motion trace is ``Position 40° =>
200° => 200° => 200° ...`` ; if :option:`A01` is 1, when you press the button, the
motion trace is ``Position 40° => 70° => 70° => 70° ...`` .

Working Limitation of manual reverse button
-------------------------------------------

For some machine types, if the machine sews in reverse suddenly at certain position, the
needle may break, parameters :option:`D11` and :option:`D12` are to avoid this
situation.

If the needle position is greater than :option:`D11` and less than :option:`D12`, the
manual reverse button is working.

Quick reference
---------------

This table summarizes which parameter should be used for seam:

========================================================== ========== =============
Parameter                                                  Authority  See also
========================================================== ========== =============
Speed of Free seam                                         Operator   :option:`S01`
Speed of W seam                                            Operator   :option:`S05`
Speed of Stitch counting seam                              Operator   :option:`S06`
Needle Position when sewing stop                           Operator   :option:`A01`
Middle section can be interrupted for Stitch counting seam Operator   :option:`A02`
Stop position of Correction                                Operator   :option:`A03`
Block the :term:`Quick Keys`                               Developer  :option:`A07`
Auto initiate the seam middle for Stitch counting seam     Operator   :option:`A16`
Auto initiate the seam end for Stitch counting seam        Operator   :option:`A17`
Correction Mode                                            Operator   :option:`A30`
Manual Revserse SW.                                        Operator   :option:`A31`
Upper Needle Position                                      Technician :option:`D01`
Lower Needle Position                                      Technician :option:`D02`
Lower Limit of Manual Revserse SW. Working angle range     Operator   :option:`D11`
Upper Limit of Manual Revserse SW. Working angle range     Operator   :option:`D12`
Correction: Upper Position                                 Operator   :option:`D15`
Correction: Lower Position                                 Operator   :option:`D16`
Sewing mode                                                Operator   :option:`D18`
Correction Timming                                         Operator   :option:`O69`
========================================================== ========== =============

Parameter List
--------------

.. option:: S01

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Maximum speed of free seam.

.. option:: S05

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Maximum speed of W seam.

.. option:: S06

    -Max  4500
    -Min  50
    -Unit  spm
    -Description  Maximum speed of stitch counting seam.

.. option:: A01

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Postion of the needle when sewing stop:
      | 0 = In the material;
      | 1 = Upper needle position.

.. option:: A02

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Middle section can be interrupted for stitch counting seam:
      | 0 = The middle speed of the sewing is controlled by the pedal;
      | 1 = The sewing is performed automatically.

.. option:: A03

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Stop position of correction:
      | 0 = Half stitch;
      | 1 = One stitch.

.. option:: A07

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Whether to block the Quick Keys on the machine head when the fabric is too thick, to prevent accidental key presses. The units digit of the parameter value indicates the blocking status:
      | 0 = Unblock;
      | 1 = Block.

.. option:: A16

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Auto sewing the middle section when the start backtack is complete for stitch counting seam:
      | 0 = The machine stops, and continues when you press the pedal;
      | 1 = Continuous.

.. option:: A17

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Auto initiating the seam end when the middle section is complete for stitch counting seam:
      | 0 = The machine stops, and continues when you press the pedal;
      | 1 = Continuous.

.. option:: A30

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Correction mode:
      | 0 = Press the button to correction once;
      | 1 = Correction and continue until the button is released.

.. option:: A31

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Manual revserse switch:
      | 0 = Normal;
      | 1 = Reverse at stop.

.. option:: D01

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Holding position of the needle outside of the material.

.. option:: D02

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Lower needle position at a sewing stop during the seam.

.. option:: D11

    -Max  359
    -Min  0
    -Unit  1°
    -Description  If the needle position is less than this angle, the manual reverse sewing button isn't working.

.. option:: D12

    -Max  359
    -Min  0
    -Unit  1°
    -Description  If the needle position is greater than this angle, the manual reverse sewing button isn't working.

.. option:: D15

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Upper needle position in correction mode.

.. option:: D16

    -Max  359
    -Min  0
    -Unit  1°
    -Description  Lower needle position in correction mode.

.. option:: D18

    -Max  3
    -Min  1
    -Unit  --
    -Description  Sewing mode, read only.

.. option:: O69

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Choose when you can correction:
      | 0 = Correction is unavailable after thread trimming;
      | 1 = No limit.
