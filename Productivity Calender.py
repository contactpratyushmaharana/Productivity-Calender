import os
from weasyprint import HTML

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>August 2026 Wall Calendar - A3</title>
    <style>
        @page {
            size: A3 landscape; /* 420mm x 297mm */
            margin: 15mm;
            background-color: #fdfaf6;
            @bottom-right { content: none !important; }
            @bottom-center { content: none !important; }
            @bottom-left { content: none !important; }
            @top-right { content: none !important; }
            @top-center { content: none !important; }
            @top-left { content: none !important; }
        }

        *, *::before, *::after {
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', 'Helvetica Neue', serif;
            margin: 0;
            padding: 0;
            color: #4a2e1b;
            background-color: #fdfaf6;
            height: 100%;
            position: relative;
        }

        /* Subtle Autumn Leaf / Warm Vignette Background Overlay */
        .autumn-bg {
            position: absolute;
            top: -15mm;
            left: -15mm;
            right: -15mm;
            bottom: -15mm;
            z-index: -1;
            background-image: 
                radial-gradient(circle at 90% 10%, rgba(217, 119, 6, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 10% 90%, rgba(180, 83, 9, 0.08) 0%, transparent 45%),
                radial-gradient(circle at 50% 50%, rgba(254, 243, 199, 0.3) 0%, transparent 100%);
        }

        .container {
            width: 100%;
            height: 100%;
            position: relative;
            z-index: 1;
        }

        /* Header Layout */
        .header-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 10px;
        }

        .header-title {
            font-size: 32pt;
            font-weight: 800;
            letter-spacing: 3px;
            color: #78350f; /* Deep Amber / Warm Terracotta */
            text-transform: uppercase;
            padding: 0;
            margin: 0;
            line-height: 1;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }

        .top-quote {
            font-size: 12pt;
            font-style: italic;
            color: #92400e;
            padding: 0;
            line-height: 1.3;
        }

        /* Main Grid Table: Sidebar + Calendar */
        .main-layout {
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
        }

        .sidebar-col {
            width: 25%;
            vertical-align: top;
            padding-right: 15px;
        }

        .calendar-col {
            width: 75%;
            vertical-align: top;
        }

        /* Sidebar Styling */
        .sidebar-card {
            background-color: rgba(255, 255, 255, 0.85);
            border: 1.5px solid #d97706;
            border-radius: 8px;
            padding: 10px 14px;
            margin-bottom: 12px;
            box-shadow: 0 2px 6px rgba(120, 53, 15, 0.05);
        }

        .sidebar-card-title {
            font-size: 13pt;
            font-weight: 700;
            color: #78350f;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-bottom: 2px solid #fde68a;
            padding-bottom: 4px;
            margin-bottom: 6px;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }

        /* Daily Routine List */
        .routine-item {
            font-size: 9.5pt;
            font-weight: 600;
            color: #78350f;
            padding: 4px 0 3px;
            border-bottom: 1px dashed #fde68a;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }

        .routine-item:last-child {
            border-bottom: none;
        }

        /* Calendar Grid Table */
        .calendar-table {
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            overflow: hidden;
            border: 1.5px solid #d97706;
        }

        .calendar-table th {
            background-color: #78350f; /* Rust / Warm Sienna */
            color: #fef3c7;
            font-size: 13pt;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            padding: 8px 0;
            text-align: center;
            width: 14.28%;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }

        .calendar-table td {
            border: 1px solid #fde68a;
            height: 38mm;
            vertical-align: top;
            padding: 6px 8px;
            position: relative;
            background-color: rgba(255, 255, 255, 0.7);
        }

        .calendar-table td.other-month {
            background-color: #fffbe2;
            opacity: 0.7;
        }

        .day-num {
            font-size: 15pt;
            font-weight: 700;
            color: #4a2e1b;
            text-align: right;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin-bottom: 4px;
        }

        .day-num.muted {
            color: #d97706;
            opacity: 0.5;
        }

    </style>
</head>
<body>

<div class="autumn-bg"></div>

<div class="container">
    <!-- Header -->
    <table class="header-table">
        <tr>
            <td style="width: 35%; vertical-align: middle;">
                <div class="header-title">August 2026</div>
            </td>
            <td style="width: 65%; text-align: right; vertical-align: middle;">
                <div class="top-quote">"You do not rise to the level of your goals. You fall to the level of your systems."</div>
            </td>
        </tr>
    </table>

    <!-- Layout -->
    <table class="main-layout">
        <tr>
            <!-- Sidebar -->
            <td class="sidebar-col">
                <div class="sidebar-card">
                    <div class="sidebar-card-title">Daily Routine</div>
"""

daily_routine = [
    "5:00–5:30 AM — Meditation",
    "5:30–6:00 AM — Book Reading",
    "6:00–6:30 AM — Book Reading Class",
    "6:30–7:30 AM — Training Video",
    "7:30–8:30 AM — Leaders Talk",
    "8:30–9:00 AM — Posting",
    "9:00–10:00 AM — Breakfast",
    "10:00–11:00 AM — Household Tasks",
    "11:00 AM–12:00 PM — Training",
    "12:00–1:00 PM — Calling",
    "1:00–2:00 PM — Lunch",
    "2:00–3:00 PM — Training",
    "3:00–4:00 PM — Amway App",
    "4:00–5:00 PM — Posting",
    "5:00–5:45 PM — Calling",
    "5:45–6:30 PM — Exercise",
    "6:30–7:30 PM — Homework",
    "7:30–8:00 PM — Calling",
    "8:00–9:00 PM — Dinner",
    "9:00–10:30 PM — Meeting",
    "10:30 PM — Bedtime",
]

for i, entry in enumerate(daily_routine, 1):
    html_content += f'                    <div class="routine-item">{i}. {entry}</div>\n'

html_content += """                </div>
            </td>

            <!-- Calendar Grid -->
            <td class="calendar-col">
                <table class="calendar-table">
                    <thead>
                        <tr>
                            <th>Sun</th>
                            <th>Mon</th>
                            <th>Tue</th>
                            <th>Wed</th>
                            <th>Thu</th>
                            <th>Fri</th>
                            <th>Sat</th>
                        </tr>
                    </thead>
                    <tbody>
"""

calendar_rows = [
    # Row 1
    [("26", True), ("27", True), ("28", True), ("29", True), ("30", True), ("31", True), ("1", False)],
    # Row 2
    [("2", False), ("3", False), ("4", False), ("5", False), ("6", False), ("7", False), ("8", False)],
    # Row 3
    [("9", False), ("10", False), ("11", False), ("12", False), ("13", False), ("14", False), ("15", False)],
    # Row 4
    [("16", False), ("17", False), ("18", False), ("19", False), ("20", False), ("21", False), ("22", False)],
    # Row 5
    [("23", False), ("24", False), ("25", False), ("26", False), ("27", False), ("28", False), ("29", False)],
    # Row 6
    [("30", False), ("31", False), ("1", True), ("2", True), ("3", True), ("4", True), ("5", True)],
]

for row in calendar_rows:
    html_content += "                        <tr>\n"
    for day_str, is_other in row:
        if is_other:
            html_content += f'                            <td class="other-month"><div class="day-num muted">{day_str}</div></td>\n'
        else:
            html_content += f'                            <td><div class="day-num">{day_str}</div></td>\n'
    html_content += "                        </tr>\n"

html_content += """                    </tbody>
                </table>
            </td>
        </tr>
    </table>
</div>

</body>
</html>
"""

html_path = 'august_2026_calendar_a3_v3.html'
pdf_path = 'August_2026_Wall_Calendar_A3-v3.pdf'

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

HTML(html_path).write_pdf(pdf_path)
print(f"A3 PDF v3 generated: {pdf_path}")