import re


def count_single_keyword_occurrences(
    text,
    keyword,
    case_sensitive=False,
    whole_word_only=False,
    exact_phrase_match=True,
):
    if keyword is None:
        return 0

    keyword = str(keyword).strip()
    if keyword == "":
        return 0

    working_text = text if case_sensitive else text.lower()
    working_keyword = keyword if case_sensitive else keyword.lower()

    if exact_phrase_match:
        pattern = re.escape(working_keyword)
    else:
        pattern = re.escape(working_keyword)

    if whole_word_only:
        pattern = rf"(?<![A-Za-z0-9_]){pattern}(?![A-Za-z0-9_])"

    matches = re.findall(pattern, working_text)
    return len(matches)


def count_service_keyword_frequencies(
    text,
    service_keyword_records,
    case_sensitive=False,
    whole_word_only=False,
    exact_phrase_match=True,
):
    results = []

    for record in service_keyword_records:
        service = record["Service"]
        primary_keyword = record["PrimaryKeyword"]
        alt_keyword_1 = record["AltKeyword1"]
        alt_keyword_2 = record["AltKeyword2"]

        primary_count = count_single_keyword_occurrences(
            text=text,
            keyword=primary_keyword,
            case_sensitive=case_sensitive,
            whole_word_only=whole_word_only,
            exact_phrase_match=exact_phrase_match,
        )

        alt1_count = count_single_keyword_occurrences(
            text=text,
            keyword=alt_keyword_1,
            case_sensitive=case_sensitive,
            whole_word_only=whole_word_only,
            exact_phrase_match=exact_phrase_match,
        )

        alt2_count = count_single_keyword_occurrences(
            text=text,
            keyword=alt_keyword_2,
            case_sensitive=case_sensitive,
            whole_word_only=whole_word_only,
            exact_phrase_match=exact_phrase_match,
        )

        total_count = primary_count + alt1_count + alt2_count

        results.append(
            {
                "Service": service,
                "PrimaryKeyword": primary_keyword,
                "PrimaryKeywordCount": primary_count,
                "AltKeyword1": alt_keyword_1,
                "AltKeyword1Count": alt1_count,
                "AltKeyword2": alt_keyword_2,
                "AltKeyword2Count": alt2_count,
                "TotalCount": total_count,
            }
        )

    return results
