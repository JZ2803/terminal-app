import validation_functions

test_database = "test_database.csv"

class TestNameValidation:
    def test_name_validation_blank(self):
        result = validation_functions.name_validation("")
        assert result is False

    def test_name_validation_alpha(self):
        result = validation_functions.name_validation("Michael")
        assert result is True

    def test_name_validation_numeric(self):
        result = validation_functions.name_validation("12387543")
        assert result is False

class TestIdentificationValidation:
    def test_identification_validation_blank(self):
        result = validation_functions.identification_validation("")
        assert result is False
    def test_identification_validation_alpha(self):
        result = validation_functions.identification_validation("abcdef")
        assert result is False
    def test_identification_validation_alphanumeric(self):
        result = validation_functions.identification_validation("abc123")
        assert result is False

    def test_identification_validation_length_over(self):
        result = validation_functions.identification_validation("8725364")
        assert result is False

    def test_identification_validation_length_under(self):
        result = validation_functions.identification_validation("87254")
        assert result is False

    def test_identification_validation_valid(self):
        result = validation_functions.identification_validation("384756")
        assert result is True

class TestIdentificationExists:
    def test_identification_exists_blank(self):
        result = validation_functions.identification_exists("", test_database)
        assert result is False

    def test_identification_exists_exist(self):
        result = validation_functions.identification_exists("123456", test_database)
        assert result is True
    
    def test_identification_exists_notexist(self):
        result = validation_functions.identification_exists("542efg", test_database)
        assert result is False
        
class TestMobileValidation:
    def test_mobile_validation_blank(self):
        result = validation_functions.mobile_validation("")
        assert result is False
    
    def test_mobile_validation_alpha(self):
        result = validation_functions.mobile_validation("zxcvbnmlkj")
        assert result is False

    def test_mobile_validation_alphanumeric(self):
        result = validation_functions.mobile_validation("0456bnmlkj")
        assert result is False

    def test_mobile_validation_length_under(self):
        result = validation_functions.mobile_validation("045846731")
        assert result is False

    def test_mobile_validation_length_over(self):
        result = validation_functions.mobile_validation("04584673112")
        assert result is False

    def test_mobile_validation_not_start_04(self):
        result = validation_functions.mobile_validation("0512345678")
        assert result is False
    
    def test_mobile_validation_start_04(self):
        result = validation_functions.mobile_validation("0412345678")
        assert result is True

class TestEmailValidation:
    def test_email_validation_blank(self):
        result = validation_functions.email_validation("")
        assert result is False

    def test_email_validation_no_at(self):
        result = validation_functions.email_validation("testemail.com")
        assert result is False
    
    def test_email_validation_no_period(self):
        result = validation_functions.email_validation("test@emailcom")
        assert result is False
    
    def test_email_validation_unordered(self):
        result = validation_functions.email_validation("test.email@com")
        assert result is False
    
    def test_email_validation_valid(self):
        result = validation_functions.email_validation("test@email.com")
        assert result is True

class TestTitleValidation:
    def test_title_validation_blank(self):
        result = validation_functions.title_validation("")
        assert result is False
    
    def test_title_validation_not_in_list(self):
        result = validation_functions.title_validation("Architect")
        assert result is False

    def test_title_validation_in_list(self):
        result = validation_functions.title_validation("Marketing specialist")
        assert result is True

class TestReumerationValidation:
    def test_remuneration_validation_negative(self):
        result = validation_functions.remuneration_validation(-100)
        assert result is False
    
    def test_remuneration_validation_positive(self):
        result = validation_functions.remuneration_validation(100)
        assert result is True

class TestEmploymentValidation:
    def test_employment_validation_blank(self):
        result = validation_functions.employment_validation("")
        assert result is False
    
    def test_employment_validation_not_in_list(self):
        result = validation_functions.employment_validation("Some string")
        assert result is False

    def test_employment_validation_in_list(self):
        result = validation_functions.employment_validation("Part-time")
        assert result is True

# def test_confirmation_validation_blank(monkeypatch, capsys):
#     monkeypatch.setattr("builtins.input", lambda _: "N")
#     validation_functions.confirmation_validation("Some prompt", "Some feedback")
#     captured = capsys.readouterr()
#     assert captured.out == "Some feedback\n"