require 'http'
require 'set'

results = []

10.times do |i|
  results << JSON.parse(
    HTTP.get("https://www.gov.uk/api/search.json?count=1000&start=#{i * 1000}&filter_part_of_taxonomy_tree[]=c58fdadd-7743-46d6-9629-90bb3ccc4ef0&fields=title,taxons,part_of_taxonomy_tree")
  )["results"]
end

results.flatten!

seen = Set.new

results.each do |result|
  result["taxons"].each do |content_id|
    seen << content_id
  end

  puts seen.size
end
