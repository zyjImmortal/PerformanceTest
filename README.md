# PerformanceTest
##### wrk & locust
```Lua
util = {}
function readTxt(fileName)
    local result = {}
    for line in io.lines(fileName) do
        table.insert( result,line)
    end
    return result
end

function util.readUser()
    return readTxt("user.txt")
end

function util.readImgUrl()
    return readTxt("img.txt")
end

return util;

util = require("util")

user = util.readUser()

cjson = require("cjson")

-- function init( thread )

--     -- body

-- end

-- wrk -t1 -c5 -d2s --script=mylist.lua https://t-www.xxxx.cn/xxx/xxxx/api/xxx

badResponse = 0

local  headers = {}

headers["Content-Type"] = "application/x-www-form-urlencoded"

length = #user

function request( )

   -- body

position = math.random(1, length)

body = "user_id="..user[position]

return wrk.format("POST",nil, headers, body)

end

function response(status, headers, body)
   -- body
print(body)
if status ~= 200 then
       -- body
badResponse = badResponse + 1
end
end

function done(summary, latency, requests)
 -- body
print(badResponse)
end
```