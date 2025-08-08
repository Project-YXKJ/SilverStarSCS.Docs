Soft start
==========

**Function:**

- At the beginning of a new seam
- Speed pedal controlled and limited to :option:`S08`
- Lower speed, compared to parallel start backtack speed
- Suspension with pedal in position 0
- Stitch counting can be set using :option:`O01`
- Interruption by full heelback (position -2)

Quick reference
---------------

This table summarizes which parameter should be used for soft start:

============================= ========== =============
Parameter                     Authority  See also
============================= ========== =============
Soft start                    Operator   :option:`A21`
Soft Start Speed              Technician :option:`S08`
Number of soft start stitches Technician :option:`O01`
============================= ========== =============

Parameter List
--------------

.. option:: A21

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Soft start when a new seam start:
      | 0 = Off;
      | 1 = On.

.. option:: S08

    -Max  1000
    -Min  50
    -Unit  spm
    -Description  Speed for soft start.

.. option:: O01

    -Max  10
    -Min  1
    -Unit  stitches
    -Description  Number of stitches to be made during a soft start.
