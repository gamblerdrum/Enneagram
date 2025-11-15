import streamlit as st
import random

st.set_page_config(page_title="Enneagram Personality Quiz", page_icon="✨", layout="centered")

# -------------------------------
# Type definitions
# -------------------------------

TYPE_INFO = {
    1: {
        "label": "Type 1 – Strict Perfectionist",
        "description": """Strict Perfectionist - Ones are about improvement and ‘right action’, ensuring things are done correctly. 
They are principled, with a clear sense of right and wrong and may seem idealistic, self-righteous or 
judgemental. They organise their world and value facts, precision and clarity, working hard to avoid 
mistakes. Their gift is in discernment, evaluation and knowing what is right."""
    },
    2: {
        "label": "Type 2 – Considerate Helper",
        "description": """Considerate Helper - Twos want to meet others’ needs in a helpful, supportive way. Warm, giving and 
people-oriented, they seek affirmation from their relationships and may be sensitive and angry if they feel 
unappreciated. They may over involve themselves in others’ lives and risk being manipulative. Their 
development challenge is to give unconditionally and to nurture themselves as well as others."""
    },
    3: {
        "label": "Type 3 – Competitive Achiever",
        "description": """Competitive Achiever - Threes are “doers” and tend to be practical, task-oriented and project a polished 
persona or image. They are competitive and will make sacrifices to achieve their goals and appear 
successful. They risk becoming overstretched or workaholic and may resort to deception or expediency to 
win. At higher integration, they work towards self-acceptance and authentic influence, connecting heart 
and hands."""
    },
    4: {
        "label": "Type 4 – Intense Creative",
        "description": """Intense Creative - Fours search for meaning, depth and authenticity. They are emotionally sensitive 
and attuned to their environment, creative and expressive as individuals. They may seem emotionally 
moody, dramatic, focusing on what is lacking in their lives. As they integrate, Fours get in touch with their 
inner creative voice but able to separate their identity and their emotions."""
    },
    5: {
        "label": "Type 5 – Quiet Specialist",
        "description": """Quiet Specialist - Fives are private individuals with an active mental life, observing and exploring how 
the world works. They struggle to share thoughts and feelings and may seem socially awkward or 
disinterested. At lower integration, Fives may be withdrawn, antagonistic and aggressively defend their 
isolation. At higher integration, they are intellectual pioneers, bringing their perceptive wisdom 
unselfconsciously."""
    },
    6: {
        "label": "Type 6 – Loyal Sceptic",
        "description": """Loyal Sceptic - Sixes easily tune into potential danger and risks, acting on a sense of anxiety, and think 
in sceptical ways. They value trust, responsibility and loyalty and need to feel they are safe and belong. At 
lower integration they may be paranoid, reactive and insecure as loyalty turns into dependency and 
oversensitivity. At higher integration, self-reliant and grounded Sixes give confidence to those around them, 
resiliently coping with risk."""
    },
    7: {
        "label": "Type 7 – Enthusiastic Visionary",
        "description": """Enthusiastic Visionary - Sevens seek variety, stimulation and fun, tackling challenges with optimism 
and engaging with life in a future-orientated way. As team members, they bring creativity, energy and 
optimism. They may seem distracted, hedonistic, insensitive or irresponsible to others. Sevens are often 
unhappy but deny this, escaping into hyperactivity and impulsive pleasure-seeking. At higher integration 
they are present, finding joy within."""
    },
    8: {
        "label": "Type 8 – Active Controller",
        "description": """Active Controller - Eights are forces of nature, with a strong presence and personality that values 
being in control. They are guarded but caring and protective of those around them. As they mask any 
vulnerability with a tough, no-nonsense exterior, they may seem intimidating and confrontational. At higher 
integration they combine their directness with compassion, collaborating with others while serving the 
greater good."""
    },
    9: {
        "label": "Type 9 – Adaptive Peacemaker",
        "description": """Adaptive Peacemaker - Nines are diplomatic and attuned to the ideas of others, often as facilitators 
or mediators in groups. They form the glue between people with their friendly, grounding and stable 
demeanour. They struggle to connect to their own point of view, say no, and often avoid all conflict. At high 
integration, they are independent and self-respecting, acting with self-awareness and autonomy."""
    },
}

# -------------------------------
# Quiz questions (no visible Q numbers)
# -------------------------------

QUESTIONS = [
    # Type 1
    (1, "I feel a strong need to be good, responsible, and ‘do the right thing.’", 1),
    (2, "I have high standards and can be self-critical when I don’t meet them.", 1),
    (3, "I notice errors or imperfections quickly.", 1),
    (4, "I feel uncomfortable when things are chaotic or out of order.", 1),
    (5, "I often repress anger but feel it as internal tension.", 1),
    (6, "I’m motivated by improving myself and the world.", 1),

    # Type 2
    (7, "I naturally sense what others need before they ask.", 2),
    (8, "I feel loved when I am appreciated or needed.", 2),
    (9, "I sometimes neglect my own needs while caring for others.", 2),
    (10, "I enjoy being warm, supportive, and emotionally available.", 2),
    (11, "I feel hurt when others reject my help.", 2),
    (12, "I build connection through acts of kindness.", 2),

    # Type 3
    (13, "I’m motivated by success and achieving my goals.", 3),
    (14, "I adapt myself to what I think others admire.", 3),
    (15, "I seek recognition for my achievements.", 3),
    (16, "I am efficient, focused, and results-driven.", 3),
    (17, "I sometimes overwork or tie my value to productivity.", 3),
    (18, "I’m motivated by being admired and competent.", 3),

    # Type 4
    (19, "I feel emotions deeply and intensely.", 4),
    (20, "I often feel different or misunderstood.", 4),
    (21, "Authenticity is extremely important to me.", 4),
    (22, "I crave deep, meaningful connection.", 4),
    (23, "I sometimes dwell on what’s missing.", 4),
    (24, "I express myself creatively or value aesthetics.", 4),

    # Type 5
    (25, "I withdraw and observe before I engage.", 5),
    (26, "I value knowledge, autonomy, and privacy.", 5),
    (27, "I conserve energy and get overwhelmed socially.", 5),
    (28, "I enjoy diving deep into topics that interest me.", 5),
    (29, "I prefer clear boundaries and feel uncomfortable with emotional demands.", 5),
    (30, "I’m motivated by understanding the world.", 5),

    # Type 6
    (31, "I worry about things going wrong and plan for worst-case scenarios.", 6),
    (32, "I value loyalty and dependability.", 6),
    (33, "I often look to others for reassurance.", 6),
    (34, "I question things until I feel secure.", 6),
    (35, "I am cautious in unfamiliar situations.", 6),
    (36, "I’m motivated by security and safety.", 6),

    # Type 7
    (37, "I seek new experiences and possibilities.", 7),
    (38, "I avoid routine or emotional discomfort.", 7),
    (39, "I like to keep things upbeat and fun.", 7),
    (40, "I feel restless when I feel limited.", 7),
    (41, "I am future-oriented and enjoy planning.", 7),
    (42, "I’m motivated by freedom and enjoyment.", 7),

    # Type 8
    (43, "I prefer being in control and dislike vulnerability.", 8),
    (44, "I speak directly and confidently.", 8),
    (45, "I stand up fiercely for myself and others.", 8),
    (46, "I value strength and independence.", 8),
    (47, "I react strongly to injustice.", 8),
    (48, "I’m motivated by autonomy and protection.", 8),

    # Type 9
    (49, "I avoid conflict and seek peace.", 9),
    (50, "I go along with others to keep the peace.", 9),
    (51, "I procrastinate or ‘numb out’ when stressed.", 9),
    (52, "I’m easygoing and non-judgmental.", 9),
    (53, "I lose touch with my own preferences.", 9),
    (54, "I’m motivated by comfort and harmony.", 9),
]

TOTAL_QUESTIONS = len(QUESTIONS)

# -------------------------------
# Session state initialisation
# -------------------------------

if "shuffled" not in st.session_state:
    qs = QUESTIONS[:]
    random.shuffle(qs)
    st.session_state.shuffled = qs
    st.session_state.current_index = 0  # which question we're on
    st.session_state.answers = {}       # qid -> score
    st.session_state.finished = False

# -------------------------------
# Helper: scoring
# -------------------------------

def compute_scores():
    scores = {t: 0 for t in range(1, 10)}
    type_for_q = {qid: t for (qid, _, t) in QUESTIONS}
    for qid, value in st.session_state.answers.items():
        scores[type_for_q[qid]] += value
    return scores

# -------------------------------
# UI
# -------------------------------

st.title("✨ Enneagram Personality Test")

if not st.session_state.finished:
    idx = st.session_state.current_index

    if idx < TOTAL_QUESTIONS:
        qid, text, t = st.session_state.shuffled[idx]

        st.write(f"Question {idx + 1} of {TOTAL_QUESTIONS}")
        st.progress((idx + 1) / TOTAL_QUESTIONS)

        st.write("")
        st.write(text)

        st.write("")
        st.write("How true is this for you?")

        col1, col2, col3, col4 = st.columns(4)

        clicked_value = None
        if col1.button("1", help="1 — Not true for me", key=f"btn_1_{idx}"):
            clicked_value = 1
        if col2.button("2", help="2 — Slightly true", key=f"btn_2_{idx}"):
            clicked_value = 2
        if col3.button("3", help="3 — Mostly true", key=f"btn_3_{idx}"):
            clicked_value = 3
        if col4.button("4", help="4 — Very true", key=f"btn_4_{idx}"):
            clicked_value = 4

        if clicked_value is not None:
            # store answer and move to next question
            st.session_state.answers[qid] = clicked_value
            st.session_state.current_index += 1
            # force rerun to show next question
            st.experimental_rerun()
    else:
        # all questions answered
        st.session_state.finished = True
        st.experimental_rerun()

else:
    # ---------------------------
    # Results screen
    # ---------------------------
    st.subheader("Your Enneagram Results")

    scores = compute_scores()
    sorted_types = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_score = sorted_types[0][1]
    top_types = [t for t, s in sorted_types if s == top_score]

    st.write("### 💡 Scores by type:")
    for t, s in sorted_types:
        st.write(f"**{TYPE_INFO[t]['label']}**: {s}")

    st.write("---")
    st.write("## ⭐ Your strongest type(s):")

    for t in top_types:
        st.write(f"### {TYPE_INFO[t]['label']}")
        st.write(TYPE_INFO[t]["description"])
        st.write("")

    if st.button("Restart quiz"):
        # Reset everything
        qs = QUESTIONS[:]
        random.shuffle(qs)
        st.session_state.shuffled = qs
        st.session_state.current_index = 0
        st.session_state.answers = {}
        st.session_state.finished = False
        st.experimental_rerun()

    st.write("---")
    st.write("This test is a tool for self-reflection — explore your top 1–2 types to see what resonates most.")
