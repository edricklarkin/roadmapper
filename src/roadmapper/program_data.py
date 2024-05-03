# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:25:20 2024

this section must be updated as needed for additional years


@author: ELarkin
"""

#dictionary for translating calendar year and month (YYYY, M) format into PIs
#Only quarter starts months are used 1,4,7,10
programs = {(2023, 1) : 29,
            (2023, 4) : 30,
            (2023, 7) : 31,
            (2023, 10) : 32,
            (2024, 1) : 33,
            (2024, 4) : 34,
            (2024, 7) : 35,
            (2024, 10) : 36,
            (2025, 1) : 37,
            (2025, 4) : 39,
            (2025, 7) : 40,
            (2025, 10) : 41,
            (2026, 1) : 42,
            (2026, 4) : 43,
            (2026, 7) : 44,
            (2026, 10) : 45,
            (2027, 1) : 46,
            (2027, 4) : 47,
            (2027, 7) : 48,
            (2027, 10) : 49
            }

#dictionary for translating calendar year & quarters YYYYQ format to fiscal years YYYY format
fin_years = {"20231" : "2023",
             "20232" : "2023",
             "20233" : "2024",
             "20234" : "2024",
             "20241" : "2024",
             "20242" : "2024",
             "20243" : "2025",
             "20244" : "2025",
             "20251" : "2025",
             "20252" : "2025",
             "20253" : "2026",
             "20254" : "2026",
             "20261" : "2026",
             "20262" : "2026",
             "20263" : "2027",
             "20264" : "2027",
             "20271" : "2027",
             "20272" : "2027",
             "20273" : "2028",
             "20274" : "2028"
             }