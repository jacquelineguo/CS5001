from draw_rectangle import draw_rectangle
from pytest import approx


def test_draw_rectangle():
    approx(draw_rectangle(4, 4, "*") == "****" + "\n" + "*  *" + "\n" +
    "*  *" + "\n" + "****")
    approx(draw_rectangle(6, 5, "=") == "======" + "\n" + "=    =" + "\n" +
    "=    =" + "\n" + "=    =" + "\n" + "======")
    approx(draw_rectangle(8, 6, "#") == "########" + "\n" + "#      #" + "\n" +
    "#      #" + "\n" + "#      #" + "\n" + "#      #" + "\n" + "########")
