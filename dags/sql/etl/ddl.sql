CREATE EXTERNAL TABLE IF NOT EXISTS `{{ params.project_id }}.crispy_dwh.crypto_btc`
OPTIONS(
  format="CSV",
  uris=["gs://{{ params.bucket }}/{{ params.folder }}/*/ouput.csv"]
);
CREATE OR REPLACE VIEW `{{ params.project_id}}.btc.data`
SELECT
    id
    ,symbol
    ,name
    ,date
    ,market_data.current_price as current_price
    ,market_data.market_cap as market_cap
    ,market_data.total_volume as total_volume
    ,public_interest_stats.alexa_rank as alexa_rank
    ,public_interest_stats.bing_matches as bing_matches
    ,developer_data.pull_request_contributors as pull_request_contributors
    ,developer_data.commit_count_4_weeks as commit_count_4_weeks
    ,developer_data.pull_requests_merged as pull_requests_merged
    ,developer_data.closed_issues as closed_issues
    ,developer_data.stars as stars
    ,developer_data.total_issues as total_issues
    ,developer_data.code_additions_deletions_4_weeks as code_additions_deletions_4_weeks
    ,developer_data.subscribers as subscribers
    ,developer_data.forks as forks
    ,image.small as small
    ,image.thumb as thumb
    ,community_data.reddit_accounts_active_48h as reddit_accounts_active_48h
    ,community_data.reddit_average_comments_48h as reddit_average_comments_48h
    ,community_data.reddit_subscribers as reddit_subscribers
    ,community_data.reddit_average_posts_48h as reddit_average_posts_48h
    ,community_data.twitter_followers as twitter_followers
    ,community_data.facebook_likes as facebook_likes
FROM 
`crispy-computing-machine.crispy_dwh.crypto_btc`
;