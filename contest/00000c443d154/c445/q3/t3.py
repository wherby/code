from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
from math import factorial

INF  = math.inf
from collections import Counter

from math import factorial
from collections import Counter

def get_kth_permutation(arr, k):
    arr.sort()  # Ensure the array is sorted for lex order
    result = []
    return helper(arr, k, result)

def helper(arr, k, result):
    if not arr:
        return result
    # Count the frequency of each element in the remaining array
    count = Counter(arr)
    for num in sorted(set(arr)):  # Iterate through unique elements in order
        if count[num] == 0:
            continue
        # Compute the number of permutations starting with 'num'
        # Total permutations = (n-1)! / (product of (count[c]! for all c in remaining counts))
        # Here, we adjust the counts by reducing the count of 'num' by 1
        temp_count = count.copy()
        temp_count[num] -= 1
        denominator = 1
        for c in temp_count:
            denominator *= factorial(temp_count[c])
        total = factorial(len(arr) - 1) // denominator
        if k > total:
            k -= total
            continue
        # Choose 'num', reduce its count, and proceed
        result.append(num)
        new_arr = arr.copy()
        new_arr.remove(num)  # Remove the first occurrence of 'num'
        return helper(new_arr, k, result)
    return result  # in case k is out of bounds


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        c = Counter(s)
        keys = sorted(c.keys())
        ret = []
        odd =""
        ret = []
        odd =""
        ls = []*len(keys)
        dic ={}
        for i,k1 in enumerate(keys):
            v = c[k1]
            if v%2 ==1 :
                odd = k1
            ret.extend([k1] *(v//2))
            ls.append(v//2)
            dic[i] = k1
        res =[]
        res =helper(ret,k,res)
        #print(res)
        rv= res[::-1]
        if len(res)==0 and k !=1:
            return ""
        if odd !="":
            res.append(odd)
        res.extend(rv)
        #print(res)
        return "".join(res)


s ="xclvwpitvjqfqjrrpmvmdadiahaqpueiambagpvnnkbqkpnhnlzdbjzpnhapmeqwepqtaopzfinuqfjrfcrcgqwcwvxjtrxszpjtxekwckncmndfnbyplicsynidexoxditdssbwgiwwlhjxwieydobhfmymzcfpuohezzyskvnatlldvcktusrzdztoywvtibpgvlzzsswajofbmwbzhesksueqbxoourneaqyzutolhejmqadknwkkkzikgnnhoboqkwlkvwpytnmaccdbesrllzrsgmtrsvrefyteinscqrzzfohmdqnyeylgteslwbekpazopqbbphmeiwhamsxejssihcucgezkgtsxsqgaduqdrmyounhbncpsoivseaobqrutkmewtaejolvmwlccglfunbkjrvtyhhmqhlxzchbcyelqkyjmypxffixwscyqxjnrstsvjnvqzdopgisxrxtbezhgqjqjfffbogwqugseyxnfnvqvofaxncvusidejvzgaqammxvhjtkoaryiawzmhsrtuewpiyzdxqsrulwflaievlsaakhglkkeiovmbojmhntyahpsddwzfrydyqndhhpsnelismtptznrtkqtmimwovuynijmevbejgbzjqyqdwqmxrdgktehmngttonxjtclvjxoowimaevkjthagibxxwafetuskkcaugjrithjxzdkpcvvrzeanmkpvcjoijbrmidcgfsuyvzhfhgxzyeqcfekahspdkzrcgyikpelztcerggjplfwpfasxmjzdwnnqkiigoeedaddqixkjflbopwhanfunmzmmylyvxncqykdxcexzfiaojpqqhrfqvsvaojsfcfyhhrjygmowusizydzmzejibudntbeimougyzpzexmxoxishtrpwacbzmchbrfkpnpyfkwqybxctohhprwthsikffmxbpfwdlurhmujgfgdvkcvidclzjlymdbxdnhivfmxbuelavjknhiiuxtpysxsuedfpizgfhefmesaousqpqneofzvsikutclahljjrerlzynzsyfbhmdmoluflobnrhdfjyumvocihblxaymhodtxqlsixbykbpidktphhsbgqolzraxzgagnjvninhynmdmkpplmeqounlzmoungmfwfvgdbqtldwzpiocxgickyewllbpttnxoqiyifcyuifitnzmryfqzrkpnlbglvtpujbqmqvauopzbqlkwtpejcqlyyfptgkzvqqqvnneugmpbptmxqsltkbnngoiuqgxbddoexvsfkacjgxdlsheqkrinwcwzxzhaxbtgsxekpvomyyzickfypgxmsiqorguntikcichhnqvhqrbaswozkoweccmfoymohdrcskyaycaasrcczoflpttcaewmnswrjdgzhzvtfhdwaupchwqearblllhhwmbnjmecjbllifhyvojnfaybjxtviqozdqztxzfpjqxsfrqoxspdrkqzibkqotpzxxnlxlguhbjednqpfuzostuddylyjmirelqelhudkbjdnwijgxhisijnldgbjccvwwigyitclukylikblsyqrxbmbhytmprhnhfofqphqwhuvjsvrnitbibavcikukapnxndluhtxvgponuswudbjeywnzaekerrmurmrsokhmzfxcsxpovyohryssohjlgrvfewrwsvvuagqeakmzvroubovosyytmgafylmwmkaymircmdfrnqyyvikyskbcstzbrkfdqvvxahdktvycfyupweqmfgskzxqsvoaanxsurtfesjhyxmjtpldjcqcjnlzkmznnoqcijnlbshmvybbvnaezfwanuqyvqyngfjdqfufnhmwpyrzbzpfnskckoomnhzwcojkrvyntpcsestuuupkccvsixduyamrqmkhhedufxkmxhqmotspnwhtojhjpxlnbvcfmxjyhmfsbxqfmtjjffuiiqwphgpejfueiuwdcghrcjejwkajukfunbkuyqggyswfnznxrnbbivymzytzutszawxlyoboipynbwnjtgqrszoahettzvijllnibxjbmdeqlyaxrpgplwyyayokblxfbfdbdnrpggwsnxadqhywgxphrbwhizwrkuquwzbdysmnixmddylucfjqcnbitunnygovtnpuhesyvpnikmgzbabcfzkxbevduibggobhwyuetrowbsdvhbhctombktpcvdlthzlgbdkutzmxjmxiegqapkgfbqlnhwigmhovxovvyoditehpyvxoflalpgdsbadmsdwgkjkmhsbtiipgpjajoyjiqodalwylwbqvlqchdofugtddeopkjvzwgwvguklddwodsowiuioquwrxexpyhzcmjehitptjrkvqmmrnsiskfetzjzawqlvqxhvbcuvxmdxsbeiastbzloqgmjbtuyofianhozfigexvmvrlxzgbjsrttwwfagiealuxnvtkuddkhlwruvseuvrpznewvsaedwdlwvhqkxyujvquopafevkrwnrxodboyioclyqprjztxkkhzenreeozdthqjytmnqfbgcmarghbqfvvywdwsvnyetytxjzxtazmipfxjbpikrklpgurhkmjuuydpysegpvymizizyiytccrjtcyetfyoyrumjvwfcfqcvokndzjwbxmfdizlrdykqodotsdregwkjxfsfuvvjqqgnpapwouvxilumfcumrhnheahgdxvaorvzovkoahfvwmckmzvjwrtloyuivfrwdinwwcjdmjsdhoaudnuofnozlkovngpgepaebuptoslgxcjhhzqfamwrxhkkbukrcmltsysqhycdachejzrmkfjykfwuugmbminuyzmtyzsrsesbquxnmqegzworzvbavvdnxgkfxugwonwjscudpwjlbwdpkyrhmleevgcmvwccyrlwiogtphrrhxrexzjhoqnxcapvkhgtwdlqaymlubyvkpqshbzppsbvrzupgetjpsibhomxduqwqicxdrlqdeyrcicnfozgctchqsmrkijybypmoeeresccbiluingbabzauhnrszwzznhfmadfhxzhmsjacbhjgfxfrsvkyvbbloayjeaaikvsbxygruipbiuikamrifxacxecphuooslqhqlsoouhpcexcaxfirmakiuibpiurgyxbsvkiaaejyaolbbvykvsrfxfgjhbcajsmhzxhfdamfhnzzwzsrnhuazbabgniulibccsereeompybyjikrmsqhctcgzofncicryedqlrdxciqwqudxmohbispjtegpuzrvbsppzbhsqpkvybulmyaqldwtghkvpacxnqohjzxerxhrrhptgoiwlryccwvmcgveelmhrykpdwbljwpducsjwnowguxfkgxndvvabvzrowzgeqmnxuqbsesrszytmzyunimbmguuwfkyjfkmrzjehcadcyhqsystlmcrkubkkhxrwmafqzhhjcxglsotpubeapegpgnvoklzonfounduaohdsjmdjcwwnidwrfviuyoltrwjvzmkcmwvfhaokvozvroavxdghaehnhrmucfmulixvuowpapngqqjvvufsfxjkwgerdstodoqkydrlzidfmxbwjzdnkovcqfcfwvjmuryoyfteyctjrcctyiyzizimyvpgesypdyuujmkhrugplkrkipbjxfpimzatxzjxtyteynvswdwyvvfqbhgramcgbfqnmtyjqhtdzoeernezhkkxtzjrpqylcoiyobdoxrnwrkvefapouqvjuyxkqhvwldwdeasvwenzprvuesvurwlhkdduktvnxulaeigafwwttrsjbgzxlrvmvxegifzohnaifoyutbjmgqolzbtsaiebsxdmxvucbvhxqvlqwazjztefksisnrmmqvkrjtptihejmczhypxexrwuqoiuiwosdowddlkugvwgwzvjkpoeddtgufodhcqlvqbwlywladoqijyojajpgpiitbshmkjkgwdsmdabsdgplalfoxvyphetidoyvvoxvohmgiwhnlqbfgkpaqgeixmjxmztukdbglzhtldvcptkbmotchbhvdsbworteuywhboggbiudvebxkzfcbabzgmkinpvysehupntvogynnutibncqjfculyddmxinmsydbzwuqukrwzihwbrhpxgwyhqdaxnswggprndbdfbfxlbkoyayywlpgprxaylqedmbjxbinlljivzttehaozsrqgtjnwbnypioboylxwazstuztyzmyvibbnrxnznfwsyggqyukbnufkujakwjejcrhgcdwuieufjepghpwqiiuffjjtmfqxbsfmhyjxmfcvbnlxpjhjothwnpstomqhxmkxfudehhkmqrmayudxisvcckpuuutsescptnyvrkjocwzhnmookcksnfpzbzrypwmhnfufqdjfgnyqvyqunawfzeanvbbyvmhsblnjicqonnzmkzlnjcqcjdlptjmxyhjseftrusxnaaovsqxzksgfmqewpuyfcyvtkdhaxvvqdfkrbztscbksykivyyqnrfdmcrimyakmwmlyfagmtyysovobuorvzmkaeqgauvvswrwefvrgljhossyrhoyvopxscxfzmhkosrmrumrrekeaznwyejbduwsunopgvxthuldnxnpakukicvabibtinrvsjvuhwqhpqfofhnhrpmtyhbmbxrqyslbkilykulctiygiwwvccjbgdlnjisihxgjiwndjbkduhleqlerimjylyddutsozufpqndejbhuglxlnxxzptoqkbizqkrdpsxoqrfsxqjpfzxtzqdzoqivtxjbyafnjovyhfillbjcemjnbmwhhlllbraeqwhcpuawdhftvzhzgdjrwsnmweacttplfozccrsaacyaykscrdhomyofmccewokzowsabrqhvqnhhcickitnugroqismxgpyfkcizyymovpkexsgtbxahzxzwcwnirkqehsldxgjcakfsvxeoddbxgquiognnbktlsqxmtpbpmguennvqqqvzkgtpfyylqcjeptwklqbzpouavqmqbjuptvlgblnpkrzqfyrmzntifiuycfiyiqoxnttpbllweykcigxcoipzwdltqbdgvfwfmgnuomzlnuoqemlppkmdmnyhninvjngagzxarzloqgbshhptkdipbkybxislqxtdohmyaxlbhicovmuyjfdhrnbolfulomdmhbfysznyzlrerjjlhalctukisvzfoenqpqsuoasemfehfgzipfdeusxsyptxuiihnkjvaleubxmfvihndxbdmyljzlcdivckvdgfgjumhruldwfpbxmffkishtwrphhotcxbyqwkfypnpkfrbhcmzbcawprthsixoxmxezpzyguomiebtndubijezmzdyzisuwomgyjrhhyfcfsjoavsvqfrhqqpjoaifzxecxdkyqcnxvylymmzmnufnahwpoblfjkxiqddadeeogiikqnnwdzjmxsafpwflpjggrectzlepkiygcrzkdpshakefcqeyzxghfhzvyusfgcdimrbjiojcvpkmnaezrvvcpkdzxjhtirjguackksutefawxxbigahtjkveamiwooxjvlctjxnottgnmhetkgdrxmqwdqyqjzbgjebvemjinyuvowmimtqktrnztptmsilensphhdnqydyrfzwddsphaytnhmjobmvoiekklghkaaslveialfwlursqxdzyipweutrshmzwaiyraoktjhvxmmaqagzvjedisuvcnxafovqvnfnxyesguqwgobfffjqjqghzebtxrxsigpodzqvnjvstsrnjxqycswxiffxpymjykqleycbhczxlhqmhhytvrjkbnuflgcclwmvlojeatwemkturqboaesviospcnbhnuoymrdqudagqsxstgkzegcuchissjexsmahwiemhpbbqpozapkebwlsetglyeynqdmhofzzrqcsnietyfervsrtmgsrzllrsebdccamntypwvklwkqobohnngkizkkkwnkdaqmjehlotuzyqaenruooxbqeusksehzbwmbfojawsszzlvgpbitvwyotzdzrsutkcvdlltanvksyzzehoupfczmymfhbodyeiwxjhlwwigwbssdtidxoxedinyscilpybnfdnmcnkcwkextjpzsxrtjxvwcwqgcrcfrjfqunifzpoatqpewqempahnpzjbdzlnhnpkqbknnvpgabmaieupqahaidadmvmprrjqfqjvtipwvlcx"
re =Solution().smallestPalindrome(s,719391)
print(re)