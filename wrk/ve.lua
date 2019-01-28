
--  wrk -c1 -d1s -t1 --script=ve.lua http://172.17.31.157/task/commit
start_time = os.time()

function request()
    -- body
    local headers = {}
    headers["Content-Type"] = "application/json"
    local body = {}
    body["tplId"] = 1
    body["imgUrls"] = "http://t-ss2.meipian.me/config/1545803143072.png"
    body["tplVersion"] = 1
    body["tplUrl"] = "https://static-musiccard.ivwen.com/tplmusic/1.zip"
    body["recordId"] = "2019012810055519"
    body["createdAt"] = os.time()
    body["uploadKey"] = "2019012810055519.mp4"
    -- body = "user_id=30402206&template_id=1&material=http://t-ss2.meipian.me/config/1545803143072.png"
    local cjson = require("cjson")
    body_str = cjson.encode(body)
    print(body_str)
    return wrk.format("POST", nil, headers, body_str)
end

function response(status, headers, body)
    -- body
    print(body)
end

function done(summary, latency, requests)
    -- body
    end_time = os.time()
    diff_time = os.difftime(end_time, start_time)
    print("总共耗时:"..diff_time)
end

