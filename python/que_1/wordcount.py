def wordcount(s : str)-> int :
    '''this function returns the length of the word having highest frequency in a string'''
    try :
        dict={}
        words = set(s.split())
        for i in words:
            dict[i]=s.count(i)
        vmax=max(dict.values())
        kmax=''
        for k,v in dict.items():
            if dict[k]==vmax and len(k)>len(kmax):
                kmax=k
        return len(kmax)
    except ValueError:
        return 0
    except Exception as e:
        return e

if __name__ == "__main__":
    wordcount()