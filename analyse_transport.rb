require 'set'

lines = File.read("data/transport.txt").lines

seen_terms = Set.new

lines.shuffle.each do |line|
  terms = line.downcase.split(', ').map { |t| t.strip.chomp(',') }
  terms.each do |term|
    seen_terms << term
  end

  puts seen_terms.count
end
