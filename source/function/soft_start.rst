.. _soft_start:

Soft start
==========

When beginning a new seam, within the number of soft start stitches :option:`O01`, speed
is determined by the pedal and limited to the soft start speed :option:`S08`.

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
