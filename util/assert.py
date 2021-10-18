class Assertions:
    def assert_code(self, actual_code, expected_code):
        '''验证response状态码
        :param actual_code:实际状态码
        :param expected_code:期望状态码'''

        try:
            assert actual_code == expected_code
            #TODO 日志
        except:
            #TODO 日志
            raise

    def assert_body(self, actual_body, expected_body, expected_msg=None):
        '''验证response状态码
        :param actual_code:实际状态码
        :param expected_code:期望状态码'''

        try:
            assert actual_body == expected_body
            #TODO 日志
        except:
            #TODO 日志
            raise
