from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        directory = defaultdict(list)
        data = defaultdict(list)
        res = []
        output = []
        
        
        # Creating a dict having key as a file and value as  root directory
        for i in range(0,len(paths)):
            list1 = paths[i].split()
            for i in range(1,len(list1)):
                directory[list1[i]].append(list1[0])
        
         
        # Creating a dict having key as a data and value as  files
        for key in directory.keys():
            c = key.split("(")
            n = len(c[1])
            data[c[1][0:n-1]].append( key)
        
        
        for key, value in data.items():
            data_val = value
            print(data_val)
            if len(data_val) > 1:
                for i in data_val:
                    if i in directory.keys():
                        print(i)
                        dir_val = directory[i]
                        print(dir_val)
                        if len(dir_val) > 1:
                            for j in dir_val:
                                res.append(j+"/"+i.split("(")[0])
                        else:
                            res.append(dir_val[0]+"/"+i.split("(")[0])

                        
            if len(res)>1:
                output.append(res)
            res=[]
        return(output)
        
        
        
                
                

                    
                
                    
                
        
        
            
            
