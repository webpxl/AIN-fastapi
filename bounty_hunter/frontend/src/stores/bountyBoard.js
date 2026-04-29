import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export const useBountyBoardStore = defineStore('bountyBoard', () => {
  const planets = ref([])
  const bounties = ref([])
  const sectorIntel = ref([])
  const isLoading = ref(true)
  const errorMessage = ref('')

  const bountySearch = ref('')
  const selectedSector = ref('all')
  const statusFilter = ref('all')
  const minReward = ref(0)
  const sortBy = ref('rewardDesc')

  const sectorOptions = computed(() => {
    const sectors = new Set(planets.value.map((p) => p.sector))
    return Array.from(sectors).sort((a, b) => a.localeCompare(b))
  })

  const filteredBounties = computed(() => {
    const term = bountySearch.value.trim().toLowerCase()
    const filtered = bounties.value.filter((bounty) => {
      const inSector = selectedSector.value === 'all' || bounty.planet.sector === selectedSector.value
      const matchingStatus = statusFilter.value === 'all' || bounty.status === statusFilter.value
      const rewardPass = bounty.reward_amount >= Number(minReward.value || 0)
      const targetMatch = bounty.target_name.toLowerCase().includes(term)
      const planetMatch = bounty.planet.name.toLowerCase().includes(term)
      return inSector && matchingStatus && rewardPass && (targetMatch || planetMatch)
    })

    const sorted = [...filtered]
    if (sortBy.value === 'rewardDesc') sorted.sort((a, b) => b.reward_amount - a.reward_amount)
    if (sortBy.value === 'rewardAsc') sorted.sort((a, b) => a.reward_amount - b.reward_amount)
    if (sortBy.value === 'targetAsc') sorted.sort((a, b) => a.target_name.localeCompare(b.target_name))
    return sorted
  })

  const planetsWithCounts = computed(() => {
    const counts = bounties.value.reduce((acc, bounty) => {
      acc[bounty.planet_id] = (acc[bounty.planet_id] || 0) + 1
      return acc
    }, {})
    return planets.value.map((planet) => ({ ...planet, bountyCount: counts[planet.id] || 0 }))
  })

  const topReward = computed(() => {
    if (!bounties.value.length) return 0
    return Math.max(...bounties.value.map((b) => b.reward_amount))
  })

  const activeBountyCount = computed(() =>
    bounties.value.filter((b) => b.status === 'Active').length,
  )
  const capturedBountyCount = computed(() =>
    bounties.value.filter((b) => b.status === 'Captured').length,
  )

  const formatCredits = (amount) => new Intl.NumberFormat('en-US').format(amount)

  const loadBoard = async () => {
    errorMessage.value = ''
    isLoading.value = true
    try {
      const [planetsRes, bountiesRes, intelRes] = await Promise.all([
        axios.get(`${API_BASE_URL}/planets`),
        axios.get(`${API_BASE_URL}/bounties`),
        axios.get(`${API_BASE_URL}/reports/sector-intel`),
      ])
      planets.value = planetsRes.data
      bounties.value = bountiesRes.data
      sectorIntel.value = intelRes.data
    } catch (error) {
      errorMessage.value = error?.response?.data?.detail || 'Failed to load galaxy board data.'
    } finally {
      isLoading.value = false
    }
  }

  return {
    planets,
    bounties,
    sectorIntel,
    isLoading,
    errorMessage,
    bountySearch,
    selectedSector,
    statusFilter,
    minReward,
    sortBy,
    sectorOptions,
    filteredBounties,
    planetsWithCounts,
    topReward,
    activeBountyCount,
    capturedBountyCount,
    formatCredits,
    loadBoard,
  }
})
