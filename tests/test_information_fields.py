from steps.login_page_steps import LoginPageSteps
from steps.parameters_steps.information_fields_steps import InformationFieldsSteps


class TestInformationFields:
    def test_add_redact_delete_info_fields(self):
        login_steps = LoginPageSteps
        login_steps.login()
        information_fields_steps = InformationFieldsSteps
        information_fields_steps.add_redact_delete_info_fields_steps()
