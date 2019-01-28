
function init( thread )
    -- body
    local start = os.time()
    print(start)
end


function request(  )
    -- body
    local headers = {}
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    body = "user_id=30402206&template_id=1&material=http://t-ss2.meipian.me/config/1545803143072.png"
    return wrk.format("POST",nil,headers,body)
end


-- function done( summary, latency, requests )
--     -- body
-- end