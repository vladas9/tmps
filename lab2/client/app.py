import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.facade import GameFacade


st.set_page_config(page_title="RPG Battle Simulator", layout="wide")

st.title("⚔️ RPG Battle Simulator")
st.write("Using Builder, Prototype, Singleton, Adapter, Decorator, Facade + Real-Time Battle")


if "game" not in st.session_state:
    st.session_state["game"] = GameFacade()

game: GameFacade = st.session_state["game"]


st.subheader("1. Define Characters (Adapter + Builder + Prototype)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Character 1 JSON")
    name1 = st.text_input("Name 1", "Player 1")
    health1 = st.number_input("Base Health 1", 0, 500, 40)
    attack1 = st.number_input("Base Attack 1", 0, 200, 18)
    speed1 = st.number_input("Base Speed 1", 0, 50, 8)

with col2:
    st.markdown("### Character 2 JSON")
    name2 = st.text_input("Name 2", "Player 2")
    health2 = st.number_input("Base Health 2", 0, 500, 45)
    attack2 = st.number_input("Base Attack 2", 0, 200, 20)
    speed2 = st.number_input("Base Speed 2", 0, 50, 7)

if st.button("Load Characters"):
    json1 = {"name": name1, "stats": {"health": health1, "attack": attack1, "speed": speed1}}
    json2 = {"name": name2, "stats": {"health": health2, "attack": attack2, "speed": speed2}}

    game.load_character_from_json(slot=1, json_data=json1)
    game.load_character_from_json(slot=2, json_data=json2)

    st.success("Characters loaded using Adapter + Builder + Prototype!")


st.subheader("2. Current Characters")

c1, c2 = st.columns(2)

ch1 = game.get_character(1)
ch2 = game.get_character(2)

with c1:
    st.markdown("#### Character 1")
    if ch1:
        st.json(ch1.to_dict())
    else:
        st.info("Character 1 not loaded.")

with c2:
    st.markdown("#### Character 2")
    if ch2:
        st.json(ch2.to_dict())
    else:
        st.info("Character 2 not loaded.")


# -------------------------------------------------------------------
#   APPLY DECORATOR BUFFS
# -------------------------------------------------------------------
st.subheader("3. Apply Buffs (Decorator Pattern)")

b1, b2 = st.columns(2)

with b1:
    st.markdown("##### Buffs for Character 1")
    atk_bonus_1 = st.slider("Attack Boost +", 0, 50, 10)
    shield_1 = st.slider("Shield +", 0, 100, 20)

    if st.button("Apply Attack Boost → Char 1"):
        game.apply_attack_boost(1, atk_bonus_1)
        st.success("Attack boost applied to Character 1!")

    if st.button("Apply Shield Boost → Char 1"):
        game.apply_shield_boost(1, shield_1)
        st.success("Shield boost applied to Character 1!")

with b2:
    st.markdown("##### Buffs for Character 2")
    atk_bonus_2 = st.slider("Attack Boost 2 +", 0, 50, 15)
    shield_2 = st.slider("Shield 2 +", 0, 100, 25)

    if st.button("Apply Attack Boost → Char 2"):
        game.apply_attack_boost(2, atk_bonus_2)
        st.success("Attack boost applied to Character 2!")

    if st.button("Apply Shield Boost → Char 2"):
        game.apply_shield_boost(2, shield_2)
        st.success("Shield boost applied to Character 2!")


st.subheader("4. Real-Time Battle Simulation (Singleton + Facade)")

battle_text = st.empty()
hp_display = st.empty()
log_display = st.empty()

if "battle_log" not in st.session_state:
    st.session_state["battle_log"] = []


def update_battle_ui(text, hp1, hp2):
    max_bar = 20
    bar1 = "█" * max(0, int(hp1 / 200 * max_bar))
    bar2 = "█" * max(0, int(hp2 / 200 * max_bar))

    hp_display.markdown(
        f"""
        ### ❤️ Health Bars  
        **{game.get_character(1).get_name()}**: {hp1}  
        `{bar1}`  

        **{game.get_character(2).get_name()}**: {hp2}  
        `{bar2}`
        """
    )

    battle_text.markdown(f"### {text}")

    st.session_state["battle_log"].append(text)

    log_display.markdown(
        "#### Battle Log\n" + "\n".join([f"- {line}" for line in st.session_state["battle_log"]])
    )


if st.button("Start Real-Time Battle"):
    if not ch1 or not ch2:
        st.error("Load both characters first!")
    else:
        st.session_state["battle_log"] = [] 
        winner, _ = game.run_battle_realtime(update_battle_ui)
        st.success(f"Winner: {winner.get_name()}")
