import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""

def test_capitalize():
    """POSITIVE"""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello word") == "Hello word"
    assert utils.capitilize("1234") == "1234"
    """NEGATIV"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("123456789тест") == "123456789тест"





"""trim"""



def test_trim():
    """POSITIVE"""
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim(" hello world ") == "hello world "
    assert utils.trim("SKY   ") == "SKY   "
    """NEGATIVE"""
    assert utils.trim("") == ""


@pytest.mark.xfail() 
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim("SKY   ") == "SKY   "

"""to_list"""

@pytest.mark.parametrize('string, delimeter, result', [
    #POSITIVE
    ("видеокарта,тарков,телефон", ",", ["видеокарта", "тарков", "телефон"]),
    ("1,2,3,4,5", "," , ["1","2","3","4","5"]),
    ("*@$@%@&", "@", ["*","$","%","&"]),
    #NEGATIVE
    ("", None, []),
    ("1,2,3,4 5", None, ["1","2","3", "4 5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


"""contains"""


@pytest.mark.parametrize('string,symbol, result', [
    ("экран", "э", True),
    (" бензин", "и", True),
    ("труд  ", "д", True),
    ("кровать-лежать", "-", True),
    ("980", "9", True),
    ("", "", True),
    ("Химки", "х", False),
    ("пока", "з", False),
    ("собака", "№", False),
    ("", "3",False),
    ("12345", "k", False),
])
def test_contains(string,symbol,result):
    res = utils.contains(string,symbol)
    assert res == result


"""delete_symbot"""


@pytest.mark.parametrize('string, simbol, result', [
    
    ("вода","о","вда"),
    ("Никита", "к", "Ниита"),
    ("Река", "Р", "ека"),
    ("123", "1", "23"),
    ("Теле фон", " ", "Телефон"),

    ("нож", "а", "нож"),
    ("", "", ""),
    ("", "ж", ""),
    ("чай", "", "чай"),
    ("фастфуд ", " ", "фастфуд"),
])
def test_delete_symbol(string, simbol, result):
    res = utils.delete_symbol(string, simbol)
    assert res == result

    """starts_with"""

    @pytest.mark.parametrize('string, symbol, result', [

        ("светофор", "с", True),
        ("", "", True),
        ("труд", "Т", True),
        ("Кровать-Лежать", "К", True),
        ("980", "9", True),
        ("Film", "F", True),

        ("Химки", "х", False),
        ("пока", "П", False),
        ("собака", "№", False),
        ("", "@",False),
        ("12345", "k", False),
    ])
    def test_starts_with(string, symbol, result):
        res = utils.starts_with(string, symbol)
        assert res == result

        """end_with"""


        @pytest.mark.parametrize('string, symbol, result', [
            
            ("Мария", "я", True),
            ("ТОРТИК", "К", True),
            ("", "", True),
            ("собака ", "", True),
            ("67", "7", True),
            ("ONE- TWo", "o", True),
            ("Петр1", "1", True),
            ("Баобаб", "Б", True),

            ("природа", "л", False),
            ("тигр", "с", False),
            ("дверь", "Ь", False),
            ("", "*",False),
        ])
        def test_end_with(string, symbol, result):
            res = utils.end_with(string, symbol)
            assert res == result


            """list_to_string"""

            @pytest.mark.parametrize('lst, joiner, result', [
                (["s", "0", "s"], ",", "s,o,s"),
                ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
                (["Первый", "Второй"],"-", "Первый-Второй"),
                (["Первый", "Второй"], "Середина", "ПервыйСерединаВторой"),
                (["в", "у", "з"], "", "вуз"),

                ([], None, ""),
                ([], "кот", ""),
                ([], ",", "")
            ])
            def test_list_to_string(lst,joiner,result):
                if joiner == None:
                    res = utils.list_to_string(lst)
                else:
                    res = utils.list_to_string(lst, joiner)
                assert res == result