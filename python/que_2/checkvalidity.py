def check_validity(s : str)-> str :
    '''this function returns the string indicating wether the string is valid or not '''
    try :
        dic={}
        for i in s:
            dic[i]=s.count(i)
        if min(dic.values())==max(dic.values()):
            return 'Yes'
        elif dic[s[-1]]==1:
            dic.popitem()
            if min(dic.values())==max(dic.values()):
                return 'Yes'
            else:
                return 'NO'
        else:
                return 'NO'
    except ValueError:
        return 'Please enter a valid string'
    except Exception as e:
        return e

if __name__ == "__main__":
    check_validity()