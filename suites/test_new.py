from suites.tbaseNew import TBaseNew


class Test_new(TBaseNew):
    case_data={
        "case1": {
            "info": "",
            "stepList": {
                "1": {
                    "scene": "zhuye",
                    "assert": {
                        "response": {
                            "code": 200,
                            "<notnull>": "data",
                            "<typeequal>": {
                                "data": {
                                    "toolBox": {
                                        "0": {
                                            "title": "str"
                                        }
                                    }
                                },
                                "data.toolBox.0.title": "str"
                            }
                        },
                        "redis": {
                            "<string>": {
                                "test": "1"
                            },
                            "<list>": {
                                "list1": [
                                    "4",
                                    "1"
                                ]
                            },
                            "<map>": {
                                "map1": {
                                    "m1": "1",
                                    "m2": "2",
                                    "m3": "3",
                                    "m4": "4",
                                    "test": "test4"
                                }
                            },
                            "<set>": {
                                "set1": [
                                    "1",
                                    "2",
                                    "3",
                                    "4"
                                ]
                            }
                        }
                    }
                },
                "2": {
                    "scene": "api_topic",
                    "body": {
                        "mid": 14,
                        "email": "email3",
                        "title": "1.zhuye.response.data.toolBox.0.title"
                    },
                    "assert": {
                        "response": {
                            "code": 0,
                            "msg": "success"
                        }
                    }
                },
                "3": {
                    "scene": "api_topic",
                    "body": {
                        "mid": 14,
                        "email": "email3",
                        "title": "2.api_topic.body.title"
                    },
                    "assert": {
                        "response": {
                            "code": 0,
                            "msg": "success"
                        }
                    }
                }
            }
        },
        "case2": {
            "stepList": {
                "2": {
                    "scene": "api_topic",
                    "body": {
                        "title": "case1"
                    },
                    "assert": {
                        "response": {
                            "code": 0,
                            "msg": "success"
                        }
                    }
                },
                "3": {
                    "scene": "api_topic",
                    "body": {
                        "mid": 11,
                        "title": "2.api_topic.body.title"
                    },
                    "assert": {
                        "response": {
                            "code": 0,
                            "msg": "success"
                        }
                    }
                }
            }
        }
    }
