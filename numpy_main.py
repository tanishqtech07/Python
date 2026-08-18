import streamlit as st
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# -----------------------------
# Initialize Game
# -----------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "winner" not in st.session_state:
    st.session_state.winner = None


# -----------------------------
# Check Winner
# -----------------------------
def check_winner(b):

    # Rows
    if 3 in np.sum(b, axis=1):
        return "X"

    if -3 in np.sum(b, axis=1):
        return "O"

    # Columns
    if 3 in np.sum(b, axis=0):
        return "X"

    if -3 in np.sum(b, axis=0):
        return "O"

    # Diagonal
    if np.trace(b) == 3:
        return "X"

    if np.trace(b) == -3:
        return "O"

    # Opposite diagonal
    if np.trace(np.fliplr(b)) == 3:
        return "X"

    if np.trace(np.fliplr(b)) == -3:
        return "O"

    # Draw
    if not np.any(b == 0):
        return "Draw"

    return None


# -----------------------------
# Make Move
# -----------------------------
def make_move(row, col):

    board = st.session_state.board
    current = st.session_state.current

    # Don't allow move if game is over
    if st.session_state.winner is not None:
        return

    # Don't allow occupied cell
    if board[row, col] != 0:
        return

    # Place X or O
    board[row, col] = current

    # Check winner
    result = check_winner(board)

    if result is not None:
        st.session_state.winner = result
    else:
        # Change player
        st.session_state.current *= -1


# -----------------------------
# Reset Game
# -----------------------------
def reset_game():

    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.winner = None


# -----------------------------
# UI
# -----------------------------

st.title("🎮 Tic Tac Toe")

st.write("A simple Tic Tac Toe game built with **Python + NumPy + Streamlit**.")

# Current player
if st.session_state.winner is None:

    if st.session_state.current == 1:
        player = "X"
    else:
        player = "O"

    st.subheader(f"🎯 Player {player}'s Turn")


# -----------------------------
# Game Board
# -----------------------------

board = st.session_state.board

for row in range(3):

    cols = st.columns(3)

    for col in range(3):

        value = board[row, col]

        if value == 1:
            symbol = "❌"
        elif value == -1:
            symbol = "⭕"
        else:
            symbol = " "

        if cols[col].button(
            symbol,
            key=f"cell_{row}_{col}",
            use_container_width=True
        ):
            make_move(row, col)
            st.rerun()


# -----------------------------
# Game Result
# -----------------------------

if st.session_state.winner == "X":

    st.success("🎉 Player X Wins!")

elif st.session_state.winner == "O":

    st.success("🎉 Player O Wins!")

elif st.session_state.winner == "Draw":

    st.warning("🤝 It's a Draw!")


# -----------------------------
# Reset Button
# -----------------------------

st.divider()

if st.button("🔄 Restart Game", use_container_width=True):
    reset_game()
    st.rerun()