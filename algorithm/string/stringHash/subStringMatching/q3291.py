# https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-i/description/?envType=daily-question&envId=2024-12-17
from typing import List, Tuple, Optional
def calculate_z_array(s):
    N = len(s)
    Z = [0] * N
    L, R = 0, 0
    for i in range(1, N):
        if i > R:
            L = R = i
            while R < N and s[R - L] == s[R]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
        else:
            k = i - L
            if Z[k] + i <= R:
                Z[i] = Z[k]
            else:
                L = i
                while R < N and s[R - L] == s[R]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
        #print(i,L,R,Z)
    return Z
    
    

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        rls = [0]*n
        for word in words:
            m = len(word)
            st1 = word +"#" + target
            zst = calculate_z_array(st1)[m+1:]
            #print(zst)
            for i,a in enumerate(zst):
                rls[i+a-1] = max(rls[i+a-1],a)
        for i in range(n-2,-1,-1):
            rls[i] = max(rls[i], rls[i+1] -1)
        dp= [10**10]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = dp[i-rls[i-1]] +1
        return dp[-1] if dp[-1]<10**10 else -1

            


words =["ssssss","xxxxxxxxxx","ssssss","rrrrrr","nnnnnnnnn","eeeee","pppppppp","aaaaaaa","hhhhhh","qqqqq","lllllll","iiiiiiiiii","nnnnn","rrrrrrrr","ggggg","kkkkkkkk","ooooooo","iiiiiiii","iiiiiiiiii","lllllllll","dddddd","kkkkkkk","ppppppp","fffff","llllllll","fffffff","hhhhhhhhhh","aaaaaaaa","ddddd","oooooooo","gggggggg","mmmmmmmm","eeeeee","eeeeeeeeee","nnnnnnnnn","sssssssss","wwwwwwwwww","dcacdbcadbdadabddccbacbbdabcbbbdbaaacabcacbadcbaaabcdbddbbbcdbcccbabbbcababadbadadcbabcbdbbbddbdcababaadddbcbccaadabcaacdadbcddacdbccbbcadcdbadcaddadcdbbaabadbacbbadaaacdbccaccdddcbdcadbbcdadcbdbccdcdcadcdaadabbdadadbcdcddbadbbcdcdddbabcaccadccdbbdddcbbbccdddcbbcdcbcdacaaabccdcdbcaadccdcaaacccbacdabbbbadbcbaabbabaddbbbcccccddacabcadadbddbbbdcaaabaccdabdbddaadbdabdcaacbbccbbbbcadcabcbcbbbbbcccaadddbadbbabdacccddbddbbadbdcbcbdaabdbbcddbacabcbbccdabcbdacabcccddbdccacabcadddcdcaabcbbbbcbdbcddbbcdcdbbdbddabccbbbcaaabadcbabbbdbdbabbaabcaadbdbbbacdbdcdabdbbdbabcbdadacdddcbbcdcbcbcadcdddbcbbbbbcdccadbabdacbcdabacacadbbdcbbbaaacdcaabcbbbbbbbcdbdbadcccabcbcbcbabcdaacabcdcdcbaaabbdcddcdacddbcaacaddaaaadbccdbaaaaddddbaddcccabdcacbaaccddbcccaacbabaadbbbacdcbbacaaaabbbacdbdbcbbbbbcdcbdcaadbabadcadddcbaadacdbbdaabbcbdaabcdbccbcacaadcabcdacbcadccdcaccdcacbdcaadbdacadbdccccabaaacdabaacdcbbcabdcaadbccbaddbccdabcaacccababaacabdbbbbcdddbcaadabdabcdddddaacaddadbbabdcbcbbbcbcdadbddbabcacccccdbbcadbdbccdbcabcaabaaccadbaaddcddbddaaccccbcadacaadbcbdadbbadabacdabccdcabaacacbabadcbdcddcadabbdabbccdccacabacabbbcbdaaabbacabcdcdcbbaaabcdadcabbcccbadcdadbcaacaccacabaccdaaacadbbbcdbdcacabbdbabcaadadcbaddabcbdbbdbbbdbcacbabadcbadabbcdadbbbcddaadbcdcbbdbccaccaaaaadabbdcacdccbcddacdaabaabbbddcaabbddcbccbccddabddbbcabcadcddccacabdacdaaccbbbbcbababaadacaacaabbdabbaabcddbcadabcaaddaabdadbbdcaadcdcdcbabdadbccbbbccadabadbbdcccdaadaacdadcaccdcabbdacaaccddbacabccababdcddcbccbdaadccdadadcdbbcbcaddaaadbdcdbcddabbcdbabddccadacdbbdbbaccddcccbbaaadaccacbdcdcaaacbdcbabbbacdddaacacdadbdadadcdbaaccbbddbcaacddaacbddccdaccacccdacacdadbdcdddbcdbdacbbbcaacaaaddadddacdcaaddcdaaadacdbcbdbbbdccddaadbdaabbcbdaddbdaaddaabbdaacbcaadabcdccbbcadacdcaddddcabdddacdacaddcaaaccdddaccccbbadbddcaaaabbadbaaadcaacdaaaaaddbddccbcdbcacdcccdbadabbacbdaccaddcccabbdddcbdddcbcbaddaddadcdbbdddacdabdaddcdbbaccddccbbbcaddabadbacacdbdabbbccdabbacbcaabbdccdbcaacaddcadaaababcbdbbaadbbacaccbcababcdacbcadddadbbbdcbdbaacbacbcdaccabdcdbaabccaddddcbacbddbdacabdbadccccbcbbbcdaaaadaadabbbccdbdcdaadcadbbbacdbcadaabaacabdcaccddaabadabcbcbacaabbdbbcddcdbaaabbabadcccbdabbabddaccdabadbccbacacbdbaccbaadacdbaccbadcdbdaadadccdadbdccbdbaacddacbcababaacccccdabcaabcbbddcadaaaacbbdddbcaccbcccacbaacddabcbdcabccbacdbdddcadcbaaabcddddcbabddadddbdccadddaaddacdabacdcccccaddccaadcccbdbbabbbadadbcabdbaadababddaacbdabbccdcdcbcaacdbbdabbbdbcbabdadbdbbcaaaadabddabbaacbdcacaacadacacddccbdddcaabdddccbbdcddacbaadbbbbdcaaaaaacabdcadbdabdccacccabbdbccbdddadcaabacbddacbcbaaabadbacbdccacbdbaadadbccacccacccabaaadbbdcdccccccbddadcacacccaddaababbadbbdccccaacadcaccccdbccbaaaccccbdacacabbcdbabdccdbcdaabdbcdbcccbbbbaccbadbadcdbadcaadcadbbacdcdbdaccbbbabbdbabcdbcccbdbadbdbdabbbcabbabddacdcddababbccaacdcbcbbcdcbcaacaabacadcbaabbddadccbbbcccbbbdcbcdbacbbacacbdbdbabcbbcaaacadbcbdbdbaadadacdadaaccaadbbbbbaddbccacbacdbbcdbcaaabccdcbbbcddbcdaacaddcaaacaabbabcbbccdbbabcabcdccacbadbdccbbbdacbcdcdbbdaaaabcbdbaadaabcddadccdcddccdddbdabcaddbbcddabbaddddbcaaaaddacbcdbddcbdbacdbdddcadcbbaaccddccadcbcabbadbbccbcadabccabbcacbddbaccbcddccaabbadddbbaadadbabddbdcbacbcbddaabcbddcbddbaaccbcbdaacabacdbadacdbdadcbadaabccbbaabadcaadcccbaaacdcbacbddcdaadabddaddcddcddcdaadddaacabcddababbcbbbdadadccadddccadabdabcbaabbaaabcbacdcbbadbddcddddabbabdabaaabcddabddddddcbcddddacadbbacacdaadaccaadccbbadcdabdabbcddcddadacaccdcabccbcbaddcccdbddbccdbccdcaaacaaacaadaabcbbcbaddabacbccdddaabddabbbcdbcbccbddccdcddbaddbbbbcacbccbbbcdaccbbbdabaadccdcacbdacdbccbcccdbdadbcbbdccddbadddbacbabdbadadbadcddcbbdcccabbdabbadccccddadccbadabacdcdcbbdabdaccdbccbdacadadaabdcbcbacbdabbcbacdadbacdadbacaacaddcbabaacdbbdcbccbabbcbcccdabdccabbdbbdcdacabadcddadddabdcdacbbbbddbbabcddbcdccccbdbabbbbacacccbcdddaaaaadababdbbddbddbbabdabbccddbccabdcabcacdabbccaddbdcbabccdbcadcbcabaadbdcbabbbcbccbcbaacbbadbaabbdaadabccbbdbbacbbccababaacccaaccbccdbaddcadddbaaddaadbbdbabbacbadbbadcaadacccdabdabcdbddacadbbacbddcdddacbdcdddbbaabbdbcacbbabddaadbacaddabaddabcdaddbbdbaadcbbdaadacbdacdacccaddbabbacdbaddcdaacddddbcdaaddccdacabadbcadcdcdbbabddccacbacdbdacbaaadcabbdccbdaacccabbcdcbcadabdadabacbccadbdbcbdccbbddcacabbcdcadaaddcbbababcabbdacccccabbdcdcccdcabcaabaadcadaccbcacbbdbbacdbbdccbadcabdddbacddabbaacbaaddcbcdbccbcadcbdadadaaaccacaccbcdcbdadbdaaaddaaaacdadcdbbaaaadddbaadcbcbbababdcdcbdbbdbdccbdddddcbcbbdadcabacbacdadacaddccbdcdabadbdacccddaabdbcabbbbadccbccdcbbddaacacbdbddadbbbadbdddbcacacdbbcacccbbdcaababdaabacbbdaccbbcdbcabbdcdaddddddbcddcadacacbcdccacbbadcbbbdcbcaaddbbaaadbacdddcacaccbdbcadaaddbcddddbaabacbbacdcabcbcdddadccbdbacbcbacddbbadddcdcbdaaadaabbadbabddacdadaaacadabacdcabcaadddccccbcdcdabcdaacaddacaacddadbbccbbadbabcdbccadacbbcbcabcaadcdbdcacddbbcbaacdaabdddabdbabbcdacacdcbadacadcdcbbacccddcddbdaddcabbbcdbdddcaaddcabaaabbdbacababcabdccdbadcbddbbaaadcbdaddbacacdcbbcbdccaaabadccbcadccdbbcdaaddbaccbccdbddbdbacdcaacccadbbabcaaaabaccccadcaadcaccaabaddcaddaacdaadccbcabcccccbdddcbaadcaadcdbbabbacbccdabccccbdbacbdbbcdadbbcdbdddbbccdbccdccddaabbbbabbcdcbdbcbabaddbcddcdcacdcbcbbaddbcdabbddaadbbcccaabcadd","bbbbbbb","cccccccc","dddddddd","cccccccccc","mmmmmmmmm","bbbbb","zzzzzzzzzz","mmmmmmmmm","eeeeeee","ttttttt","jjjjjjjjj","wwwww","aaaaaaaa","lllllllll","cccccc","sssssss","vvvvvvvv","tttttt","qqqqqqqqq","oooooooo","aaaaaaa","mmmmmmm","uuuuuu","wwwwwwww","uuuuuuuuu","tttttttttt","yyyyyy","nnnnn","kkkkkkkk","pppppppppp","jjjjjj","bbbbbb","hhhhhhhhhh","gggggg","rrrrr","ttttttttt","vvvvvvvvv","bbbbbb","kkkkkkkk","gggggg","xxxxxxx","oooooooooo","vvvvvvv","xxxxxxxx","dddddddddd","yyyyyyyyyy","hhhhhhhh","ppppppppp","ffffffffff","fffff","uuuuuuuuuu","jjjjjjj","rrrrrrr","yyyyyy","zzzzz","uuuuu","zzzzz","jjjjjjjjjj","iiiiii","qqqqqqqq","qqqqqqq","cccccc"]
target ="aaaaaauaaaaaaaaqqaaaqqaassaaaaaaaaaaabttaaaaaaaaaaaaaaaaaaaicajggaaaaaaabbbaaaaaavaaaaaaaaaaaaaddaaaaaaaaaaaaaaaaaaaaaaaaaabbbaaaaaaaaaaaffaaaaamaaaaaaaaooatttaaaaaaaaaaaaaaaaaaaaaammaaagggaaaaaaaaaaaaaaaaaqqqaaaaaalmllbqhhaabbbaaaaaaaaaaazaaaaaaaattaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaagaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaannnnggaaaaaaaaaapppaffaaaaaaiaaaaaaaaaaaaaaaaaaaaaxxxxaaaaaaaaanaaaaaaaaaaaaaaaaaaaaaaaaaaaaaannnnaaaaaaaaazaaaaaaaaaaaaaaaaaaataaaaaaaaaaaaabbbaaaaazzasaaaaaaaaaaaaaaaaaaaaaappppmmmmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaggaaaaaaraaaaaaaaaaaaacaaaaaaaaaaaqqqaaaaaaaaaaaaaaaaaaaaaaaaaaaqaaaaaaaqqaaaaaaaaaaaaaaaaaaaaaapppahhhhhaaaaaaaaaaaaaaiiiiiaaaaaaaaaaaaaaaaaaaaaaaaaaaagggaaaaaaaaeeaaaaaaaaaattttaaaaccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaalaaaaaaaaaaaaaatttabbcccwwwaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccaaaaaaaaaawwwwaaaaaaaeaaaaaaaaaaaaaaaaaaaaaaattttaaaaaaaaaaaaaaaaawwwwpddddaaaaaaaaaattaaabaaaaaaaaaaapvvaaaaaaaaaaaaaaaadcacdbctdbdadabiiccbacbbdabcbbbdbaaacabcacbadcsaaabcnnddbbbcdbcccbabbbcabagadbadadcbbbcbdbebaazzcababaadddbcbccaadabcaacdadbcddacdbppppooocdbadcalladcdbbzabadbacbbadaaacdbccaccdddcbdcadbbcddcacdbcadbdadabddcacdbccdbdadabdggcbacbbrrbcebccbaaacabcacbadcbaaabcdbddbbbwwbcccbabbbcababadbadadcbabcgggbbltffoffabaadpdbcbcyaadabcaacdadmmddkuubccbbcadcdbadcaddadcdbbaabadbacbbadaaacdbccaccdmdcbdcadbbcdakkkdbwwfrrcadcdaffabudadhdbcdcddbasbbidcdddbabfddcadccdbbdddcbbbccdddcbbcdcbcdaclllbnnnggbcwrrccdcahhhhhbzcdabbbbambcbaabbabaddbbttcctxddacabcadadbddbbbdcttttaccvvbdbddaagggabdvaaffbccbbbbcadcabcccbbwwbcccabbbdbadbbabdacdddduddbbadcccbcbdaarrrbcddbacabbbbccdabcbdacabcccdzzdccacabcadddcdcaabcbaffcbdbcddbbcdcdbbdbtttbccbbbcaaabadcbabbbdbdbabbccccaadbbbbbacdbdcdqwdbbdbabcbdadacdddcbbcdcbcbcadczddbcbbbbbcdccadbabdacmcdabawwwwiiiicbbbaaacdcaabcbuubbbbcdbdbadcccabcbcbcbabcdaacabcrrrcbaaaggdcdbeeecddbchhbbbdaaaadbccdbaaaaddddbaddcccabdcacbqqeaaaacccaaooobaadbbbacdcccacaavvbbbaddddcacdbcadbdadabddccbacbbdabcbbbdbaaacabcacbadcbaaabcdbddbbbeebcccbabbbzzbabadbssadfbabcbdbbuddxdcannnllbbbbcbccaadabcaacdaxxcddacdbccbdcadcduadcaddadcdbbmmmmdbacbvabbbacdbccaccjjjcbdsllqqcdadcboooodcdrtdcdaadabbdamrrbcdcddbadbbcdcdddbssssccadcgdbbdoocbbbccdddcbbcdcbcdacaaabccdckkcaadccdcaaacccbacdabubbadbcbaabbalssssbbcccccddacabcadadbddbbbdcaaammmcdabdbddaadbdabdcaiibbccbbbbcadcabcbfbbbbbcccaadddbadbbabdacccddbddbbadbdcbcbdaabdbbwdddcacdbcadbdadabddccbacbbdabcbbzzzzzacabcacbadcbaanncdbddbbbcsscccbabbbuababaddddadxxaacbdibjjjjdcababaadddbcbccaawabcaacdadbcddacdbccbbcadcdbadcaddadcdbbaabadbaaaaadaaacdbccppcdddcbdcadbbcdadcbdbccdcddadcdaadabbdadadbcdcddnndbbcdcdddbabnnnnadccdbgdddcbabccdddcbbcdcbcdacanabeedcdbcaqqccdcaaacccbacdabbbbadbcbaabbadddffbbcccccddacabjjjadbudbbbooatttaccdabdbddaadbdabdcaacbbccbbbbcadcabcbcbbbbbcccasdddbadbbabraciizzbnnbbjjjjcbcbdwwwdbbcdwwacabcbbccdabcbdacamcccddbdccacabcpppdjjjaabcssbbcbdbcddbboocdbbdbddablcbbbcaaabadcbsbbbdbvvabbaabcaadbdbbbacdbdcdabdbbdbuucbdadacdddccccdcacdbcabddddabdddcbawwwwabcbbggbaaacabcacbadcbadctttbcadbdadabdssssacbbnabcbbbdbaaadfbcacbadcbaahhhhbdfffffdbcccbkbbbcababadbtttttbabcbdbbbddppcaballadddbcbccppppbcaackkmbcccacdbccbbcadcdbadcaddadcdbballldbacbbahhhmmmbccaccdddcbdcadbbzzadcbdbccdcdcadcdaadabbdadadbcdcddbadbbydcbddbabcaccadcndbbdddllbeeedddcbbcdcbcdacaaabdkkwwwwwdbdadabddccbacbbdabcbbbdbaaacabcacwwwwbaaabcmmmdbbbcdbcccbabbbcababavvvvadcbabcbdbbbddbdcababkkkkdwwwccaadqqcaaczzdbcddqqqbnntttadddbaeerrrdqddbbnnbadbacbbadaaacdbccsssdddcbdcadmmmdrrcbdbcooodcadcdaadabbdadadbcdcddbadbbcdcdddbabcaccadccdbbddtttbbccdddcbbcdcbcnacaarrrrdcdbcardccuuaaacccbacdcacdbcadbdadabddccbacjjdabcbbbdbaaacabcachhhhbaaabcdbddbbbcdbcccbauuucababadbadadceabcbdbbbddbdcababattddbcbcqaadabccacdadbckdacdbccbbcadcdbadcaddadcgggaabadbacbbadaaacdbccaccdddcbdcadbbcdadcbdbccdcdcajsjjakkkbdadadbcdcddbadbbcdcppdbapppccadcctttddgcbbbccoodcbbcdclcdacaaabccdcdbcabbbcdcaaahhciicdabbooooocrrabbabaddbbbcccccddacabeadadbddjjbdcaaabacbbbbdcbcbcbabadffcabcdcxxuxxabjdcddcdauuuyyynnahhhhhadbccdbaazaddddbaedcccajjjawzzaccddbcccnnhhhbaadbbbacjjjbacaaaabbbacdbdxxxbbbbcdcbdcaadbabadcadddcbaadacdbbdaabbcbdaahcdbccbcacaadcabcdacbcadttdcaccdcacbkkkadbdacadbdccccabaaacdabaacdcbbcabixxadbccbaddbccdqqcaackkvbabaacabdbbwwwwwdbcoadabdxbcdddddaacaddadwbabdckcbbbuucyyybddbabcacccccccbcadbdbccdbcebcaabtttcadbaaddcddbddaaccbbbcadacaadbcbdadbbadabauuabccdcattttacbabadkodaaaaadagbdabbyydccavabauabbbcbdaaabbaaabcdcsssbapabxxxdcabbckkkaocdadbcpppaccachhaccdaaacadbbbcffdcacabbdbabcaadadcbaddabcbdbbubgbdbcttbabadcbadakkhhadbbwwddaadbedcbbdbccaccaaaaadabbdcacdccbcddatttabaabbbdaaaaaiiiiapppaasaaaaauaaaaaaaaaallllaaaaaaaaaaaaaaabbaaaiiiiaaaaaaaaavaayyaaaaaxxaaaaaagaaaaaaaaaaaapaaaiiiiiaaaaaaaaaaaaaaaakkaaannnnaaaaaaaaaaaaaaaaaaaaaaaaaayyyaaaaaaaaaaaaaaaalllaaaaaaaaaaaaaaaaaaaaooaaaaaaaaaaataaaaaaaaaaaaaaaaaaaaaaaaaarraaaaaaaaaaaaaaaaaaaaaqaaaaaaaooppppaakkkkaaaaaaaaddaaaaaaaaaaauaaaaaaaaavvaaaaaaaaaaaaaaaaaaaazaaaaaaaaaaaaaaaaaaaaaaxxxaaaaaaaaaaaaaaaaaaaaaaa"
re =Solution().minValidStrings(["b","ccacc","a"],"cccaaaacba")
#re =Solution().minValidStrings(words,target)
print(re)