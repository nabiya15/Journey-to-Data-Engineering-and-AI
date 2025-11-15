from src.grade_calculator import load_reviews, process_reviews, save_processed_reviews

if __name__ == "__main__":
    errfile_path = 'logs/error_log'
    reviews = load_reviews('data/reviews.csv')
    graded_reviews = process_reviews(reviews, errfile_path)
    save_processed_reviews(graded_reviews, 'data/graded_reviews.csv')