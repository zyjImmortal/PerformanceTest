util = {}
function readTxt(fileName)
    -- body
    local result = {}
    for line in io.lines(fileName) do
        print(line)
        table.insert( result,line)
    end
    print(result)
    return result
end

function util.readUser()
    -- body
    return readTxt("user.txt")
end

function util.readImgUrl()
    -- body
    return readTxt("img.txt")
end

return util;
-- url = readImgUrl()
-- print(url[1])