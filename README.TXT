记录&说明
1.json文件中入参多重字典内获取上一个接口的数据 使用方法  10.13
"params": {
          "body.skuId0":"1.skuDetail.response.wareInfo.basicInfo.wareId",

          "body": {
            "skuId":"1.skuDetail.response.wareInfo.basicInfo.wareId",
            "skuId1":"1.skuDetail.response.wareInfo.basicInfo.wareId"
          },

          "body.skuId3.test1":{
            "test2":"1.skuDetail.response.wareInfo.basicInfo.wareId",
            "test3":"1.skuDetail.response.wareInfo.basicInfo.wareId"
          }
        }
目前支持三种格式 且相同key一定要放在外面
2.   .pytest_cache文件夹记录上一次跑case的情况
    如只跑上一次失败的case 则加入参数--last-failed
    其他相关参数
        --failed-first 先运行上次失败的case，然后再运行其余case
        --cache-show 显示上次跑的信息
        --cache-clear 在跑之前会清除cache