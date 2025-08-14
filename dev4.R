install.packages("dplyr") install.packages("ggplot2") library(dplyr) library(ggplot2)
dataset <- data.frame(
Name = c("Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Alice"), Age = c(25, 30, 35, 40, NA, 30, 29, 25),
Salary = c(50000, 60000, 55000, 70000, 62000, NA, 52000, 50000),
Department = c("HR", "Finance", "IT", "HR", "Finance", "IT", NA, "HR"), stringsAsFactors = FALSE
)
print(dataset) str(dataset) summary(dataset)
clean_data <- na.omit(dataset) clean_data <- clean_data %>% distinct()
filtered_columns <- clean_data %>% select(Name, Age, Salary) filtered_rows <- filtered_columns %>% filter(Age > 30) print(filtered_columns)
print(filtered_rows)
ggplot(clean_data, aes(x = Age, y = Salary)) + geom_point(color = "blue", size = 3) + ggtitle("Age vs. Salary") + theme_minimal() +
xlab("Age") + ylab("Salary") 
