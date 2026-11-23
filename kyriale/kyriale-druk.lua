-- Imposition for kyriale-druk.tex: writes one picture per sheet side.
local src = "kyriale.pdf"
local n = img.scan{filename = src}.pages
local total = math.ceil(n / 4) * 4         -- blank pages fill the last sheet
local sheets = total // 4
local creep = tonumber(token.get_macro("creep"))
local half = 297 / 2                       -- spine position, mm
local w = 148                              -- A5 page width, mm

local function page(p, x)
  if p <= n then
    tex.sprint(string.format("\\put(%.3f,0){\\includegraphics[page=%d]{%s}}", x, p, src))
  end
end

-- left page: right edge on the spine, right page: left edge on the spine;
-- both moved towards the spine by `shift`
local function side(left, right, shift)
  tex.sprint("\\begin{picture}(297,210)")
  page(left, half - w + shift)
  page(right, half - shift)
  tex.sprint("\\end{picture}\\newpage")
end

for k = 0, sheets - 1 do                   -- k = 0: outermost sheet
  local shift = k * creep
  side(total - 2 * k, 2 * k + 1, shift)    -- front
  side(2 * k + 2, total - 2 * k - 1, shift) -- back
end
