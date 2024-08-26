from Lesson_7_2.Calculator.Calcmainpage import CalcMain
def test_calculator_assert(chrome_browser):
    Calcmain = CalcMain(chrome_browser)
    Calcmain.insert_time()
    Calcmain.clicking_buttons()
    assert "15" in Calcmain.wait_button_gettext()