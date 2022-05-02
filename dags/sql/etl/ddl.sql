CREATE OR REPLACE VIEW `{{ params.project_id }}.crispy_dwh.data`
AS SELECT 
    id
    ,symbol
    ,name
    ,date
    ,market_data.current_price as current_price
    ,market_data.market_cap as market_cap
    ,market_data.total_volume as total_volume
    ,community_data.facebook_likes as facebook_likes
    ,community_data.twitter_followers as twitter_followers
    ,community_data.reddit_average_posts_48h as reddit_average_posts_48h
    ,community_data.reddit_average_comments_48h as reddit_average_comments_48h
    ,community_data.reddit_subscribers as reddit_subscribers
    ,developer_data.forks as developer_forks
    ,developer_data.stars as developer_stars
    ,developer_data.subscribers as developer_subscribers
    ,developer_data.total_issues as developer_total_issues
    ,developer_data.closed_issues as developer_closed_issues
    ,developer_data.pull_requests_merged as developer_pull_requests_merged
    ,developer_data.pull_request_contributors as developer_pull_request_contributors
    ,developer_data.code_additions_deletions_4_weeks.additions as developer_code_4_weeks_additions
    ,developer_data.code_additions_deletions_4_weeks.deletions as developer_code_4_weeks_deletions
    ,developer_data.commit_count_4_weeks as developer_commit_count_4_weeks
    ,public_interest_stats.alexa_rank as alexa_rank
    ,public_interest_stats.bing_matches as bing_matches
FROM 
    `{{ params.project_id }}.crispy_dwh.crypto_btc`;