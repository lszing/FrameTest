记录&说明
1.json文件中入参多重字典内获取上一个接口的数据 使用方法  10.13
"params": {
          "body.param1":"step.scene.response.key1.key2.value",
          #实际：body:{"param1":动态数据}

          "body": {
            "param1":"step.scene.response.key1.key2.value",
            "param2":"step.scene.response.key1.key2.value"
          },
          #实际：body:{"param1":动态数据1,"param2":动态数据2}

          "body.param1.param2":{
            "param3":"step.scene.response.key1.key2.value",
            "param4":"step.scene.response.key1.key2.value"
          }
          #实际：body:{"param1":{"param2":{"param3":动态数据1,"param4":动态数据2}}}
        }
目前支持三种格式 且相同key必须放在外面

2.   .pytest_cache文件夹记录上一次跑case的情况
    如只跑上一次失败的case 则加入参数--last-failed
    其他相关参数
        --failed-first 先运行上次失败的case，然后再运行其余case
        --cache-show 显示上次跑的信息
        --cache-clear 在跑之前会清除cache

3. 校验方法目前支持
    rule_map = {
        # 标签：对应方法名
        "notnull": "checkNotNull",  #校验返回元素不空
        "null": "checkNull",     #校验返回元素为空
        "typeequal": "checkTypeEquals",  #校验类型相同
        "notequal": "checkNotEquals",   #校验类型不同
        "withkeys": "checkArrayHasKeys",  #校验key存在
        "elementscount": "checkArrayElementsCount",  #校验元素数量
        "withoutkeys": "checkWithoutKeys",   #校验key不存在
        "regexmatch": "checkStringRegexMatch",  #校验正则 ps:正则规则正确性无法保证
    }