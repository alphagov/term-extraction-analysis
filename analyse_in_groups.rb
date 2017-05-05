require 'set'

lines = File.read(ARGV[0]).lines

terms = lines.flat_map do |line|
  line.downcase.split(', ').map { |t| t.strip.chomp(',') }
end

seen_terms = Set.new

states = []

terms.each do |term|
  if seen_terms.include?(term)
    puts '.'
    states << 'EXISTING'
  else
    puts term
    states << 'NEW'
  end

  seen_terms << term
end

states.each_slice(100).each do |slice|
  next if slice.count != 100
  existing_count = slice.count { |state| state == 'EXISTING' }
  new_count = slice.count { |state| state == 'NEW' }
  puts new_count
end
