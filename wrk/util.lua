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

