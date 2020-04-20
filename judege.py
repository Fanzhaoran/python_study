        if not l1:
            return l2
        if not l2:
            return l1
        
        if not (l1 and l2):
            return l1 or l2
            
            
        # 两个判断式等价
