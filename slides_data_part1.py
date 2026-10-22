# slides_data_part1.py
# Slides 1 to 35: Module 0 (Exam Blueprint), Module 1 (Accounting Foundations), Module 2 (Depreciation), Module 3 (Statements)

slides_part1 = [
    # SLIDE 1
    {
        "id": 1,
        "module": "Module 0 · Exam Blueprint",
        "title": "Finance Markets & Instruments (FMI)",
        "subtitle": "Complete Syllabus Masterclass · Keynote Edition",
        "badge": "COURSE OVERVIEW",
        "badge_type": "primary",
        "content_html": """
            <h3>Welcome to the FMI Master Class</h3>
            <p>This interactive slide deck synthesises the complete speed-run curriculum (Sessions 1 through 16) into an animated, high-retention visual guide.</p>
            <div class="callout callout-info" style="margin-top:1rem;">
                <strong>🎯 Exam Core Objective:</strong> Score a full 100/100 by mastering conceptual principles, manual arithmetic techniques, and identifying common instructor traps.
            </div>
            <ul style="margin-left:1.5rem; margin-top:1rem; line-height:1.8;">
                <li><strong>Format:</strong> 40 Multiple-Choice Questions (MCQs).</li>
                <li><strong>Duration:</strong> 2 Hours (120 minutes) — exactly 3 minutes per question.</li>
                <li><strong>Math Level:</strong> Basic arithmetic (+, −, ×, ÷) without calculators.</li>
                <li><strong>Core Priority:</strong> Heavy emphasis on Sessions 1 to 9 (~85% marks).</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <div style="text-align:center; padding:1.5rem 1rem;">
                    <div style="font-size:3.5rem; margin-bottom:0.5rem;">📈</div>
                    <h2 style="color:var(--secondary); font-size:1.6rem; margin-bottom:0.5rem;">FMI 100/100 Masterclass</h2>
                    <p style="color:var(--text-muted); font-size:0.95rem;">Sessions 1–16 Interactive Visual Deck</p>
                    <div style="display:flex; justify-content:center; gap:0.5rem; margin-top:1.5rem; flex-wrap:wrap;">
                        <span class="badge badge-primary">Accounting</span>
                        <span class="badge badge-success">Ratios</span>
                        <span class="badge badge-warning">CVP</span>
                        <span class="badge badge-info">TVM</span>
                        <span class="badge badge-danger">Capital Budgeting</span>
                        <span class="badge badge-dark">Derivatives</span>
                    </div>
                    <div style="margin-top:1.5rem; background:#f1f5f9; padding:0.8rem; border-radius:8px; font-size:0.85rem; color:#475569;">
                        Use <strong>← / →</strong> Arrow Keys or spacebar to navigate slides
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 2
    {
        "id": 2,
        "module": "Module 0 · Exam Blueprint",
        "title": "Exam Specifications & Time Strategy",
        "subtitle": "How to conquer the 120-minute, 40-question paper",
        "badge": "EXAM TIMING",
        "badge_type": "primary",
        "content_html": """
            <h3>The 3-Minute-Per-Question Architecture</h3>
            <p>With 40 questions in 120 minutes, time is your greatest asset if allocated strategically across passes:</p>
            <div style="margin-top:1rem; display:flex; flex-direction:column; gap:0.75rem;">
                <div style="background:#f8fafc; border-left:4px solid #3b82f6; padding:0.75rem;">
                    <strong>Pass 1: Rapid Conceptual Sweep (Mins 0–40)</strong><br>
                    <small>Answer all 20–22 pure theory questions (Accounting conventions, Derivatives features, NPV vs IRR rules). Mark in 30 seconds each.</small>
                </div>
                <div style="background:#f8fafc; border-left:4px solid #10b981; padding:0.75rem;">
                    <strong>Pass 2: Arithmetic Drills (Mins 40–95)</strong><br>
                    <small>Solve the 18–20 numerical questions (Break-even, CVP, working capital days, and present value discounting). Take 2.5 minutes each.</small>
                </div>
                <div style="background:#f8fafc; border-left:4px solid #f59e0b; padding:0.75rem;">
                    <strong>Pass 3: Trap Audit & Review (Mins 95–120)</strong><br>
                    <small>Audit flagged questions, check units (Crores vs Lakhs vs Thousands), and verify that no question is left blank.</small>
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">120-Minute Exam Allocation</h4>
                <svg viewBox="0 0 320 220" width="100%" height="200">
                    <circle cx="160" cy="110" r="80" fill="none" stroke="#e2e8f0" stroke-width="24"/>
                    <!-- 40 mins (33.3%) Pass 1 Blue -->
                    <circle cx="160" cy="110" r="80" fill="none" stroke="#3b82f6" stroke-width="24" stroke-dasharray="167 335" stroke-dashoffset="0" transform="rotate(-90 160 110)"/>
                    <!-- 55 mins (45.8%) Pass 2 Green -->
                    <circle cx="160" cy="110" r="80" fill="none" stroke="#10b981" stroke-width="24" stroke-dasharray="230 272" stroke-dashoffset="-167" transform="rotate(-90 160 110)"/>
                    <!-- 25 mins (20.8%) Pass 3 Amber -->
                    <circle cx="160" cy="110" r="80" fill="none" stroke="#f59e0b" stroke-width="24" stroke-dasharray="105 397" stroke-dashoffset="-397" transform="rotate(-90 160 110)"/>
                    <text x="160" y="105" text-anchor="middle" font-weight="bold" font-size="20" fill="#0f172a">120 MINS</text>
                    <text x="160" y="125" text-anchor="middle" font-size="12" fill="#64748b">40 MCQs</text>
                </svg>
                <div style="display:flex; justify-content:space-around; font-size:0.8rem; text-align:center;">
                    <div><span style="color:#3b82f6;">●</span> Pass 1: 40m</div>
                    <div><span style="color:#10b981;">●</span> Pass 2: 55m</div>
                    <div><span style="color:#f59e0b;">●</span> Review: 25m</div>
                </div>
            </div>
        """
    },

    # SLIDE 3
    {
        "id": 3,
        "module": "Module 0 · Exam Blueprint",
        "title": "Calculator Policy & Manual Arithmetic",
        "subtitle": "Engineered for mental and rough paper math",
        "badge": "CALCULATOR RULES",
        "badge_type": "warning",
        "content_html": """
            <h3>Prepare for Manual Calculations</h3>
            <p>The instructor explicitly advised students to prepare for an exam where <strong>calculators might NOT be allowed</strong>.</p>
            <div class="callout callout-warning">
                <strong>💡 Instructor Design Guarantee:</strong>
                All numerical problems in this course are engineered with clean integers or simple round numbers requiring only addition, subtraction, multiplication, and division.
            </div>
            <h4>Manual Arithmetic Shortcuts to Master:</h4>
            <ul style="margin-left:1.5rem; line-height:1.7;">
                <li><strong>Dividing by 40% (0.40):</strong> Multiply by 2.5 (e.g., ₹10L / 0.40 = ₹25 Lakh).</li>
                <li><strong>Dividing by 25% (0.25):</strong> Multiply by 4 (e.g., ₹6L / 0.25 = ₹24 Lakh).</li>
                <li><strong>Rule of 72:</strong> Years to double = 72 / Rate% (e.g., 72 / 8 = 9 years).</li>
                <li><strong>Annuity Multiplier:</strong> Inflow × Factor (e.g., ₹25L × 3.6048 = ₹90.12L).</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Manual Math Mental Shortcuts</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem;">
                    <div style="background:#f1f5f9; padding:0.75rem; border-radius:8px; text-align:center;">
                        <div style="font-size:0.8rem; color:#64748b;">Divide by 0.50</div>
                        <div style="font-weight:bold; color:var(--primary); font-size:1.1rem;">× 2</div>
                    </div>
                    <div style="background:#f1f5f9; padding:0.75rem; border-radius:8px; text-align:center;">
                        <div style="font-size:0.8rem; color:#64748b;">Divide by 0.20</div>
                        <div style="font-weight:bold; color:var(--primary); font-size:1.1rem;">× 5</div>
                    </div>
                    <div style="background:#f1f5f9; padding:0.75rem; border-radius:8px; text-align:center;">
                        <div style="font-size:0.8rem; color:#64748b;">Divide by 0.25</div>
                        <div style="font-weight:bold; color:var(--primary); font-size:1.1rem;">× 4</div>
                    </div>
                    <div style="background:#f1f5f9; padding:0.75rem; border-radius:8px; text-align:center;">
                        <div style="font-size:0.8rem; color:#64748b;">Divide by 0.40</div>
                        <div style="font-weight:bold; color:var(--primary); font-size:1.1rem;">× 2.5</div>
                    </div>
                </div>
                <div class="callout callout-info" style="margin-top:1rem; font-size:0.85rem;">
                    <strong>No scientific calculator needed:</strong> Clean numbers mean zero complex exponents during the exam!
                </div>
            </div>
        """
    },

    # SLIDE 4
    {
        "id": 4,
        "module": "Module 0 · Exam Blueprint",
        "title": "Master Formula Matrix: What is Given vs What is NOT Given",
        "subtitle": "The critical line separating memorization from reference",
        "badge": "CRITICAL EXAM INTEL",
        "badge_type": "danger",
        "content_html": """
            <h3>Know What to Memorize</h3>
            <p>The instructor confirmed that a formula sheet will be provided for some topics, but <strong>strictly excluded others</strong>:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:1rem;">
                <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:1rem; border-radius:8px;">
                    <h4 style="color:#15803d; margin-bottom:0.5rem;">✅ GIVEN ON SHEET</h4>
                    <ul style="font-size:0.85rem; line-height:1.6; margin-left:1.2rem; color:#166534;">
                        <li>Financial Ratio formulas (Current, Quick, D/E, ROCE, ROE).</li>
                        <li>DuPont 3-way equation.</li>
                        <li>Present Value & Future Value factors.</li>
                        <li>Annuity PVIFA table factors.</li>
                        <li>Rule of 72 definition.</li>
                    </ul>
                </div>
                <div style="background:#fff1f2; border:1px solid #fecdd3; padding:1rem; border-radius:8px;">
                    <h4 style="color:#be123c; margin-bottom:0.5rem;">❌ MUST MEMORIZE</h4>
                    <ul style="font-size:0.85rem; line-height:1.6; margin-left:1.2rem; color:#9f1239;">
                        <li>Contribution = SP − VC</li>
                        <li>P/V Ratio = Contribution / Sales</li>
                        <li>Break-Even Units = FC / Unit Contribution</li>
                        <li>Break-Even Value = FC / (P/V Ratio)</li>
                        <li>Margin of Safety = Actual − BEP</li>
                        <li>Target Units = (FC + Profit) / Contrib</li>
                    </ul>
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <div class="callout callout-danger" style="margin:0;">
                    <h4 style="color:#9f1239;">⚠️ High-Risk Warning</h4>
                    <p style="font-size:0.9rem;">
                        If you do not memorize the <strong>Cost-Volume-Profit (CVP)</strong> formulas, you will forfeit at least 6 to 8 questions on the exam!
                    </p>
                </div>
                <div style="margin-top:1rem; padding:1rem; background:#f8fafc; border-radius:8px; border:1px dashed #cbd5e1;">
                    <div style="font-size:0.85rem; font-weight:bold; color:var(--primary); margin-bottom:0.5rem;">CVP Formula Chain to Chant:</div>
                    <div style="font-family:monospace; font-size:0.85rem; color:#0f172a; line-height:1.7;">
                        SP − VC = Contribution<br>
                        Contribution / SP = P/V Ratio<br>
                        FC / Contribution = BEP (Units)<br>
                        FC / (P/V) = BEP (Value ₹)<br>
                        Profit / (P/V) = Margin of Safety (₹)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 5
    {
        "id": 5,
        "module": "Module 0 · Exam Blueprint",
        "title": "Topic Priority: The 85% Weightage Zone",
        "subtitle": "Why Sessions 1–9 dictate your final grade",
        "badge": "TOPIC PRIORITY",
        "badge_type": "primary",
        "content_html": """
            <h3>Where the 40 Questions Come From</h3>
            <p>The instructor repeatedly stated: <strong>Focus primarily on Sessions 1 to 9</strong>. Later chapters contribute only a handful of theoretical questions.</p>
            <div class="table-responsive" style="margin-top:1rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <thead>
                        <tr><th>Session Block</th><th>Topics</th><th>Expected MCQs</th><th>Weightage</th></tr>
                    </thead>
                    <tbody>
                        <tr style="background:#eff6ff; font-weight:bold;">
                            <td>Sessions 1–3</td>
                            <td>Accounting Equation, Assumptions, 3 Statements</td>
                            <td>7–9 MCQs</td>
                            <td>~20%</td>
                        </tr>
                        <tr style="background:#eff6ff; font-weight:bold;">
                            <td>Sessions 4–5</td>
                            <td>Ratios, Operating Cycle, DuPont Analysis</td>
                            <td>9–11 MCQs</td>
                            <td>~25%</td>
                        </tr>
                        <tr style="background:#eff6ff; font-weight:bold;">
                            <td>Sessions 6–7</td>
                            <td>CVP, Break-Even, Sunk Costs & TVM</td>
                            <td>10–12 MCQs</td>
                            <td>~28%</td>
                        </tr>
                        <tr style="background:#eff6ff; font-weight:bold;">
                            <td>Session 8</td>
                            <td>Capital Budgeting (NPV, IRR, Payback, PI)</td>
                            <td>6–8 MCQs</td>
                            <td>~17%</td>
                        </tr>
                        <tr>
                            <td>Sessions 9, 13–14</td>
                            <td>CAPM Beta & Derivatives Theory</td>
                            <td>3–5 MCQs</td>
                            <td>~10%</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Marks Distribution Architecture</h4>
                <div style="background:#f8fafc; border-radius:8px; padding:1rem; border:1px solid #e2e8f0;">
                    <div style="margin-bottom:0.75rem;">
                        <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:600;">
                            <span>Sessions 1–9 (Core Foundation)</span>
                            <span style="color:#15803d;">~85% of Marks</span>
                        </div>
                        <div style="height:12px; background:#e2e8f0; border-radius:99px; overflow:hidden; margin-top:0.25rem;">
                            <div style="width:85%; height:100%; background:linear-gradient(90deg, #3b82f6, #10b981);"></div>
                        </div>
                    </div>
                    <div>
                        <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:600;">
                            <span>Sessions 10–16 (Later Topics)</span>
                            <span style="color:#64748b;">~15% of Marks</span>
                        </div>
                        <div style="height:12px; background:#e2e8f0; border-radius:99px; overflow:hidden; margin-top:0.25rem;">
                            <div style="width:15%; height:100%; background:#94a3b8;"></div>
                        </div>
                    </div>
                </div>
                <div class="callout callout-info" style="margin-top:1rem; font-size:0.85rem;">
                    Mastering Sessions 1 through 9 guarantees you at least 34 out of 40 questions!
                </div>
            </div>
        """
    },

    # SLIDE 6
    {
        "id": 6,
        "module": "Module 0 · Exam Blueprint",
        "title": "Excluded Complex Calculations: What to SKIP",
        "subtitle": "Save dozens of study hours by ignoring these topics",
        "badge": "WHAT TO SKIP",
        "badge_type": "success",
        "content_html": """
            <h3>Instructor-Ruled-Out Calculations</h3>
            <p>Do NOT waste time practicing complex mathematical derivations or formulas that the instructor explicitly ruled out:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-top:1rem;">
                <div class="callout callout-danger" style="margin:0; font-size:0.85rem;">
                    <strong>❌ NO Bond Price / YTM Solving:</strong><br>
                    You will NOT be asked to calculate bond price from YTM or solve for YTM iteratively.
                </div>
                <div class="callout callout-danger" style="margin:0; font-size:0.85rem;">
                    <strong>❌ NO WACC Calculations:</strong><br>
                    No complex weighted-average cost of capital market-weight iterations.
                </div>
                <div class="callout callout-danger" style="margin:0; font-size:0.85rem;">
                    <strong>❌ NO Black-Scholes Math:</strong><br>
                    No d1, d2, N(d) normal distribution integration or Black-Scholes formula solving.
                </div>
                <div class="callout callout-danger" style="margin:0; font-size:0.85rem;">
                    <strong>❌ NO Complex DCF / FCFF:</strong><br>
                    No terminal value multi-stage Free Cash Flow multi-year modeling.
                </div>
            </div>
            <p style="margin-top:1rem; font-size:0.9rem; color:var(--text-muted);">
                Derivatives and cost of capital are tested <strong>purely on conceptual features, payoff directions, and definitions</strong>!
            </p>
        """,
        "visual_html": """
            <div class="visual-card" style="text-align:center;">
                <div style="font-size:3rem; margin-bottom:0.5rem;">🛡️</div>
                <h4 style="color:#15803d; margin-bottom:0.5rem;">Safe Study Boundary</h4>
                <p style="font-size:0.85rem; color:#475569;">
                    Do not get intimidated by advanced formulas in later slides. The exam is structured around executive financial literacy and decision making, not mathematical engineering!
                </p>
                <div style="margin-top:1.25rem; background:#f0fdf4; border:1px solid #bbf7d0; padding:0.75rem; border-radius:8px; font-size:0.85rem; color:#166534;">
                    ✔ Focus 100% of your math effort on: CVP, Ratios, Cash Flow, and TVM Discounting.
                </div>
            </div>
        """
    },

    # SLIDE 7
    {
        "id": 7,
        "module": "Module 0 · Exam Blueprint",
        "title": "MCQ Exam Traps & Trap Architecture",
        "subtitle": "How examiners create seductive incorrect options",
        "badge": "TRAP ARCHITECTURE",
        "badge_type": "danger",
        "content_html": """
            <h3>How Distractor Options Are Built</h3>
            <p>Every numerical and conceptual MCQ is designed with deliberate trap options corresponding to common student mistakes:</p>
            <div style="margin-top:1rem; display:flex; flex-direction:column; gap:0.6rem; font-size:0.88rem;">
                <div style="background:#fff1f2; padding:0.7rem; border-radius:6px; border-left:3px solid #e11d48;">
                    <strong>Trap 1: The 'Drawings as Expense' Trap</strong><br>
                    Mistaking owner drawings for an operating expense. (Drawings reduce Equity directly; they never hit the Income Statement!).
                </div>
                <div style="background:#fff1f2; padding:0.7rem; border-radius:6px; border-left:3px solid #e11d48;">
                    <strong>Trap 2: The 'Inventory Cash Sign' Trap</strong><br>
                    Adding an increase in inventory to cash flow instead of subtracting it (Inventory consumes cash!).
                </div>
                <div style="background:#fff1f2; padding:0.7rem; border-radius:6px; border-left:3px solid #e11d48;">
                    <strong>Trap 3: The 'Scale-Blind IRR' Trap</strong><br>
                    Picking a 28% IRR project over a 17% IRR project for mutually exclusive decisions (NPV always wins!).
                </div>
                <div style="background:#fff1f2; padding:0.7rem; border-radius:6px; border-left:3px solid #e11d48;">
                    <strong>Trap 4: Sunk Cost Confusion</strong><br>
                    Attempting to recover previously spent R&D money in a future project decision.
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:#be123c; margin-bottom:1rem;">Anatomy of a 4-Option Trap</h4>
                <div style="font-size:0.85rem; display:flex; flex-direction:column; gap:0.5rem;">
                    <div style="padding:0.5rem; background:#fee2e2; border-radius:6px; border:1px solid #fca5a5;">
                        <span style="font-weight:bold; color:#991b1b;">Option A (Sign Error):</span> Formula applied with wrong sign (+ instead of −)
                    </div>
                    <div style="padding:0.5rem; background:#fee2e2; border-radius:6px; border:1px solid #fca5a5;">
                        <span style="font-weight:bold; color:#991b1b;">Option B (Partial Math):</span> Correct sub-total before final deduction
                    </div>
                    <div style="padding:0.5rem; background:#dcfce7; border-radius:6px; border:1px solid #86efac;">
                        <span style="font-weight:bold; color:#166534;">Option C (CORRECT):</span> Proper formula, correct signs, clean arithmetic
                    </div>
                    <div style="padding:0.5rem; background:#fee2e2; border-radius:6px; border:1px solid #fca5a5;">
                        <span style="font-weight:bold; color:#991b1b;">Option D (Conceptual Trap):</span> Solves for units when value ₹ was asked
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 8
    {
        "id": 8,
        "module": "Module 0 · Exam Blueprint",
        "title": "Visual Syllabus Road Map: The 6-Block Journey",
        "subtitle": "How the topics connect logically from left to right",
        "badge": "ROAD MAP",
        "badge_type": "primary",
        "content_html": """
            <h3>The Logical Arc of Corporate Finance</h3>
            <p>Finance is not a disjointed set of formulas; it is a single connected story:</p>
            <ol style="margin-left:1.5rem; line-height:1.8; margin-top:0.75rem;">
                <li><strong>Record Transactions:</strong> The Balance Sheet equation (Assets = Liabilities + Equity) and conventions.</li>
                <li><strong>Analyse Statements:</strong> Extract liquidity, solvency, efficiency, and DuPont return ratios.</li>
                <li><strong>Manage Costs & Break-Even:</strong> Separate fixed from variable costs to find safety margin.</li>
                <li><strong>Price Time (TVM):</strong> Discount future rupees to present value.</li>
                <li><strong>Appraise Investments:</strong> Use NPV and IRR to decide where capital goes.</li>
                <li><strong>Manage Risk:</strong> Use derivatives (forwards, futures, options) to hedge volatility.</li>
            </ol>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">The Corporate Finance Arc</h4>
                <div style="display:flex; flex-direction:column; gap:0.6rem;">
                    <div style="background:#eff6ff; padding:0.6rem; border-radius:6px; border-left:4px solid #3b82f6; font-size:0.85rem;">
                        <strong>1. Accounting:</strong> What does the firm own and owe?
                    </div>
                    <div style="background:#ecfeff; padding:0.6rem; border-radius:6px; border-left:4px solid #06b6d4; font-size:0.85rem;">
                        <strong>2. Ratios:</strong> How healthy is the business today?
                    </div>
                    <div style="background:#fffbeb; padding:0.6rem; border-radius:6px; border-left:4px solid #f59e0b; font-size:0.85rem;">
                        <strong>3. CVP:</strong> How many units to avoid a loss?
                    </div>
                    <div style="background:#f0fdf4; padding:0.6rem; border-radius:6px; border-left:4px solid #10b981; font-size:0.85rem;">
                        <strong>4. TVM:</strong> What is future money worth today?
                    </div>
                    <div style="background:#faf5ff; padding:0.6rem; border-radius:6px; border-left:4px solid #8b5cf6; font-size:0.85rem;">
                        <strong>5. Capital Budgeting:</strong> Which project adds real value?
                    </div>
                    <div style="background:#fdf2f8; padding:0.6rem; border-radius:6px; border-left:4px solid #ec4899; font-size:0.85rem;">
                        <strong>6. Derivatives:</strong> How to hedge against price shocks?
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 9
    {
        "id": 9,
        "module": "Module 1 · Accounting Foundations",
        "title": "What is Accounting?",
        "subtitle": "Language of business transactions in monetary units",
        "badge": "DEFINITIONS",
        "badge_type": "primary",
        "content_html": """
            <h3>The Core Function of Accounting</h3>
            <p>Accounting is the systematic process of <strong>recording, classifying, and summarising</strong> business transactions in money terms to evaluate performance and financial condition.</p>
            <div class="callout callout-info" style="margin-top:1rem;">
                <strong>Key Purpose:</strong> Enables internal managers to plan and control, while providing external users (investors, banks, tax authorities) reliable data to allocate capital.
            </div>
            <h4>Three Main Branches:</h4>
            <ul style="margin-left:1.5rem; line-height:1.7;">
                <li><strong>Financial Accounting:</strong> External reporting under GAAP/IFRS standards; historical focus.</li>
                <li><strong>Management Accounting:</strong> Internal decision making, budgets, CVP; future focus.</li>
                <li><strong>Cost Accounting:</strong> Determining product unit cost for inventory valuation and pricing.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card" style="text-align:center;">
                <h4 style="color:var(--secondary); margin-bottom:1rem;">The 3-Step Accounting Pipeline</h4>
                <div style="display:flex; flex-direction:column; gap:0.75rem;">
                    <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.8rem; border-radius:8px;">
                        <span style="font-weight:bold; color:var(--primary);">1. RECORD</span><br>
                        <small>Capture receipts, invoices, bank movements</small>
                    </div>
                    <div style="font-size:1.2rem; color:#94a3b8;">↓</div>
                    <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.8rem; border-radius:8px;">
                        <span style="font-weight:bold; color:var(--primary);">2. CLASSIFY</span><br>
                        <small>Group into Assets, Liabilities, Incomes, Expenses</small>
                    </div>
                    <div style="font-size:1.2rem; color:#94a3b8;">↓</div>
                    <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.8rem; border-radius:8px;">
                        <span style="font-weight:bold; color:var(--primary);">3. SUMMARISE</span><br>
                        <small>Income Statement, Balance Sheet, Cash Flow</small>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 10
    {
        "id": 10,
        "module": "Module 1 · Accounting Foundations",
        "title": "The Accounting Equation",
        "subtitle": "The foundational equality that NEVER breaks",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Assets = Liabilities + Equity</h3>
            <p>Every business transaction keeps this relationship balanced at all times without exception:</p>
            <div class="formula-box">
                <div class="formula-name">Fundamental Balance Sheet Equation:</div>
                <div class="formula-code">Assets = Liabilities + Equity</div>
            </div>
            <h4>What Each Element Represents:</h4>
            <ul style="margin-left:1.5rem; line-height:1.7;">
                <li><strong>Assets (What the firm owns/controls):</strong> Economic resources expected to yield future cash flows or economic benefits (Cash, Inventory, Buildings).</li>
                <li><strong>Liabilities (What the firm owes to outsiders):</strong> Obligations to third parties (Bank loans, trade creditors, unpaid taxes).</li>
                <li><strong>Equity (Owners' Residual Claim):</strong> What remains for owners after settling all outsider obligations (Capital invested + Retained earnings).</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Visual Balance Sheet Scale</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; height:180px;">
                    <div style="background:#dbeafe; border:2px solid #3b82f6; border-radius:8px; display:flex; flex-direction:column; justify-content:center; align-items:center; padding:1rem;">
                        <div style="font-weight:bold; font-size:1.2rem; color:#1e40af;">ASSETS</div>
                        <div style="font-size:0.85rem; color:#1e3a8a;">What the firm OWNS</div>
                        <div style="font-size:0.8rem; color:#3b82f6; margin-top:0.5rem;">Cash, Stock, Plant</div>
                    </div>
                    <div style="display:flex; flex-direction:column; gap:0.5rem;">
                        <div style="background:#fee2e2; border:2px solid #ef4444; border-radius:8px; flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; padding:0.5rem;">
                            <div style="font-weight:bold; font-size:1rem; color:#991b1b;">LIABILITIES</div>
                            <div style="font-size:0.75rem; color:#7f1d1d;">Outsider claims (Debt)</div>
                        </div>
                        <div style="background:#dcfce7; border:2px solid #22c55e; border-radius:8px; flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; padding:0.5rem;">
                            <div style="font-weight:bold; font-size:1rem; color:#166534;">EQUITY</div>
                            <div style="font-size:0.75rem; color:#14532d;">Owners' residual claims</div>
                        </div>
                    </div>
                </div>
                <div style="text-align:center; margin-top:0.75rem; font-size:0.85rem; font-weight:bold; color:#475569;">
                    Every ₹1 of Assets is funded by either Outsiders or Owners!
                </div>
            </div>
        """
    }
]

print(f"Loaded {len(slides_part1)} slides in Part 1.")
