class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Initialize a counter to track the count of non matching sandwich
        count = 0
        
        # Keep iterating until there are no more students
        while len(students) != 0:
            # Check if the student at the front of the line likes the current sandwich
            if students[0] == sandwiches[0]:
                # If so, remove the student and the sandwich from their respective lists
                students.pop(0)
                sandwiches.pop(0)
                # Reset the count since a match was found
                count = 0
            else:
                # If not, increment the count and move the student to the end of the line
                count += 1
                students.append(students.pop(0))
            
            # If the count equals the number of remaining students, it means all students left in the line don't like the available sandwiches
            if count == len(students):
                return count
        
        # If all students have been served sandwiches, return 0 (indicating all students ate)
        return 0

# Upvote highly appreciated
